"""Desenho do mundo com Pygame, separado de suas regras."""

import pygame

from evolife.config import (
    BACKGROUND_COLOR,
    CREATURE_COLOR,
    CREATURE_RADIUS,
    FOOD_COLOR,
    FOOD_RADIUS,
)
from evolife.world import World


class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def draw(self, world: World) -> None:
        """Desenhe comida e criaturas, sem avançar a simulação."""
        self.screen.fill(BACKGROUND_COLOR)
        for food in world.foods:
            pygame.draw.circle(
                self.screen,
                FOOD_COLOR,
                (round(food.x), round(food.y)),
                FOOD_RADIUS,
            )
        for creature in world.creatures:
            pygame.draw.circle(
                self.screen,
                CREATURE_COLOR,
                (round(creature.x), round(creature.y)),
                CREATURE_RADIUS,
            )
