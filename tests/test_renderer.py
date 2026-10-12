"""Verifique círculos, fundo e independência entre desenho e atualização."""

import pygame

from evolife.config import BACKGROUND_COLOR, CREATURE_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH
from evolife.renderer import Renderer
from evolife.world import World


def test_renderer_draws_population_without_changing_state():
    world = World()
    initial_state = [vars(creature).copy() for creature in world.creatures]
    screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill((255, 255, 255))
    Renderer(screen).draw(world)

    assert [vars(creature) for creature in world.creatures] == initial_state
    assert tuple(screen.get_at((0, 0)))[:3] == BACKGROUND_COLOR
    for creature in world.creatures:
        center = (round(creature.x), round(creature.y))
        assert tuple(screen.get_at(center))[:3] == CREATURE_COLOR


def test_renderer_clears_previous_frame_even_with_empty_population():
    world = World()
    screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    renderer = Renderer(screen)
    renderer.draw(world)
    previous_centers = [
        (round(creature.x), round(creature.y)) for creature in world.creatures
    ]
    world.creatures.clear()
    renderer.draw(world)
    for center in previous_centers:
        assert tuple(screen.get_at(center))[:3] == BACKGROUND_COLOR
