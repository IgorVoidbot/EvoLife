"""Verifique o ciclo de vida real do SDL e os eventos da Sprint 0."""

import os
import subprocess
import sys
from pathlib import Path

import pygame
import pytest

from main import main


@pytest.mark.parametrize(
    "closing_event",
    [pygame.event.Event(pygame.QUIT), pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)],
    ids=["fechar-janela", "escape"],
)
def test_closing_events_release_display(monkeypatch, closing_event):
    original_get = pygame.event.get

    def get_events():
        pygame.event.post(closing_event)
        return original_get()

    monkeypatch.setattr(pygame.event, "get", get_events)

    assert main() == 0
    assert not pygame.display.get_init()
    assert pygame.display.get_surface() is None


def test_window_redraws_black_and_remains_responsive(monkeypatch):
    original_flip = pygame.display.flip
    frames = []

    def inspect_frame():
        screen = pygame.display.get_surface()
        assert screen.get_size() == (800, 600)
        assert pygame.display.get_caption()[0] == "EvoLife"
        for position in ((0, 0), (400, 300), (799, 599)):
            assert tuple(screen.get_at(position)) == (0, 0, 0, 255)
        original_flip()
        frames.append(1)
        # O quadro seguinte precisa limpar a superfície outra vez.
        screen.fill((255, 255, 255))
        if len(frames) == 3:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        else:
            # Uma tecla sem ação na Sprint 0 não pode interromper o loop.
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))

    monkeypatch.setattr(pygame.display, "flip", inspect_frame)

    assert main() == 0
    assert len(frames) == 3
    assert not pygame.display.get_init()


@pytest.mark.parametrize("operation", ["set_mode", "flip"])
def test_display_is_released_after_error(monkeypatch, operation):
    def fail(*args, **kwargs):
        raise pygame.error("falha de vídeo simulada")

    monkeypatch.setattr(pygame.display, operation, fail)

    with pytest.raises(pygame.error, match="falha de vídeo simulada"):
        main()

    assert not pygame.display.get_init()


def test_keyboard_interrupt_releases_display(monkeypatch):
    def interrupt():
        raise KeyboardInterrupt

    monkeypatch.setattr(pygame.event, "get", interrupt)

    assert main() == 0
    assert not pygame.display.get_init()


def test_import_does_not_open_window():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import main, pygame; assert not pygame.display.get_init(); "
            "assert pygame.display.get_surface() is None",
        ],
        cwd=Path(__file__).resolve().parents[1],
        env=os.environ.copy(),
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert result.returncode == 0, result.stdout + result.stderr
