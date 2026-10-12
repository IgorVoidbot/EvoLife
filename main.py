"""Entrada da aplicação EvoLife — somente a fundação da Sprint 0."""

import pygame

from evolife.config import (
    BACKGROUND_COLOR,
    MAX_FPS,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)


def main() -> int:
    """Abra a janela, processe eventos e libere o Pygame ao encerrar."""
    try:
        # A Sprint 0 precisa apenas de vídeo e eventos, sem inicializar áudio.
        pygame.display.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return 0

            screen.fill(BACKGROUND_COLOR)
            pygame.display.flip()
            clock.tick(MAX_FPS)
    except KeyboardInterrupt:
        return 0
    finally:
        pygame.quit()


if __name__ == "__main__":
    raise SystemExit(main())
