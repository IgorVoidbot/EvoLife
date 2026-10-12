"""Verifique círculos, fundo e independência entre desenho e atualização."""

import pygame

from evolife.config import (
    BACKGROUND_COLOR,
    CREATURE_COLOR,
    FOOD_COLOR,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from evolife.creature import Creature
from evolife.food import Food
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
    world.foods.clear()
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


def test_renderer_draws_food_with_no_population_and_does_not_change_state():
    world = World()
    world.creatures.clear()
    world.foods = [Food(100.0, 100.0)]
    rng_state = world.random.getstate()
    screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    renderer = Renderer(screen)
    renderer.draw(world)
    assert tuple(screen.get_at((100, 100)))[:3] == FOOD_COLOR
    assert world.foods == [Food(100.0, 100.0)]
    assert world.random.getstate() == rng_state
    world.foods.clear()
    renderer.draw(world)
    assert tuple(screen.get_at((100, 100)))[:3] == BACKGROUND_COLOR


def test_dead_creature_disappears_after_world_update():
    world = World()
    world.creatures = [Creature(100.0, 100.0, 0.0, 40.0, energy=0.001)]
    world.foods.clear()
    screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    renderer = Renderer(screen)
    renderer.draw(world)
    assert tuple(screen.get_at((100, 100)))[:3] == CREATURE_COLOR
    world.update(1 / 60)
    renderer.draw(world)
    assert world.creatures == []
    assert tuple(screen.get_at((100, 100)))[:3] == BACKGROUND_COLOR


def test_renderer_displays_newborn_without_advancing_lifecycle_or_counters():
    world = World()
    world.creatures = [Creature(400, 300, 0, 40, energy=120, age_seconds=20)]
    world.foods.clear()
    world.update(1 / 60)
    assert world.births_total == 1
    previous = [vars(creature).copy() for creature in world.creatures]
    counters = (world.births_total, world.deaths_total)
    screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    Renderer(screen).draw(world)
    for creature in world.creatures:
        assert tuple(screen.get_at((round(creature.x), round(creature.y))))[:3] == CREATURE_COLOR
    assert [vars(creature) for creature in world.creatures] == previous
    assert (world.births_total, world.deaths_total) == counters
