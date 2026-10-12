"""Execute os testes de janela sem depender de um desktop ou áudio."""

import pygame
import pytest


@pytest.fixture(autouse=True)
def isolated_display(monkeypatch):
    pygame.quit()
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")
    monkeypatch.setenv("SDL_AUDIODRIVER", "dummy")
    yield
    pygame.quit()
