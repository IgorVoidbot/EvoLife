"""Eventos, tempo fixo e renderização da aplicação EvoLife."""

import math

import pygame

from evolife.config import (
    FIXED_DT,
    MAX_FPS,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)
from evolife.renderer import Renderer
from evolife.world import World


def main() -> int:
    """Abra a janela, processe eventos e libere o Pygame ao encerrar."""
    try:
        # Janela e eventos não precisam inicializar o subsistema de áudio.
        pygame.display.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        world = World()
        renderer = Renderer(screen)
        clock = pygame.time.Clock()
        accumulator = 0.0

        while True:
            accumulator += clock.tick(MAX_FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return 0

            # Um quadro pode avançar zero, um ou vários passos lógicos.
            # isclose evita perder um passo por arredondamento de floats.
            while accumulator >= FIXED_DT or math.isclose(accumulator, FIXED_DT):
                world.update(FIXED_DT)
                accumulator -= FIXED_DT

            renderer.draw(world)
            pygame.display.flip()
    except KeyboardInterrupt:
        return 0
    finally:
        pygame.quit()


if __name__ == "__main__":
    raise SystemExit(main())
