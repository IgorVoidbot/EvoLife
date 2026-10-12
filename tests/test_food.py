"""Alimento inicial, busca, exploração, consumo e reposição da Sprint 2."""

import math
import random

import pytest

from evolife.config import FIXED_DT, FOOD_RADIUS, MAX_FOOD_COUNT
from evolife.creature import Creature
from evolife.food import Food
from evolife.world import World


def empty_world():
    world = World()
    world.creatures.clear()
    world.foods.clear()
    return world


def test_initial_food_has_75_units_inside_the_map():
    state = random.getstate()
    world = World()
    assert len(world.foods) == 75
    assert len({(food.x, food.y) for food in world.foods}) == 75
    for food in world.foods:
        assert FOOD_RADIUS <= food.x <= world.width - FOOD_RADIUS
        assert FOOD_RADIUS <= food.y <= world.height - FOOD_RADIUS
    assert random.getstate() == state


def test_nearest_visible_food_changes_direction_and_position():
    world = empty_world()
    creature = Creature(100, 100, math.pi, 40, vision=50)
    world.creatures = [creature]
    world.foods = [Food(140, 100), Food(100, 125), Food(100, 151)]
    world.update(0.5)
    assert creature.direction == pytest.approx(math.pi / 2)
    assert (creature.x, creature.y) == pytest.approx((100, 120))
    assert world.foods == [Food(140, 100), Food(100, 151)]


@pytest.mark.parametrize("distance, visible", [(50, True), (50.001, False)])
def test_vision_boundary_is_inclusive(distance, visible):
    creature = Creature(100, 100, math.pi, 40, vision=50, wander_remaining=2)
    rng = random.Random(42)
    state = rng.getstate()
    creature.steer(FIXED_DT, [Food(100 + distance, 100)], rng)
    assert creature.direction == pytest.approx(0 if visible else math.pi)
    assert rng.getstate() == state


def test_equal_distance_targets_use_first_food_in_list():
    creature = Creature(100, 100, 0, 40)
    creature.steer(FIXED_DT, [Food(100, 140), Food(140, 100)], random.Random(1))
    assert creature.direction == pytest.approx(math.pi / 2)


def test_wandering_changes_direction_only_after_interval_without_target():
    creature = Creature(100, 100, 0, 40, wander_remaining=1.5)
    rng = random.Random(42)
    expected_rng = random.Random(42)
    expected_direction = expected_rng.uniform(0, math.tau)
    expected_interval = expected_rng.uniform(1, 3)
    creature.steer(1, [], rng)
    assert creature.direction == 0
    assert creature.wander_remaining == pytest.approx(0.5)
    creature.steer(0.5, [], rng)
    assert creature.direction == expected_direction
    assert creature.wander_remaining == expected_interval
    assert 1 <= creature.wander_remaining <= 3
    # Durante a perseguição, o intervalo de exploração não avança.
    creature.steer(0.5, [Food(100, 140)], rng)
    assert creature.wander_remaining == expected_interval


def test_initial_wandering_intervals_follow_prd():
    assert all(1 <= creature.wander_remaining <= 3 for creature in World().creatures)


@pytest.mark.parametrize("distance, eaten", [(9.9, True), (10, True), (10.1, False)])
def test_food_collision_uses_both_radii(distance, eaten):
    world = empty_world()
    creature = Creature(100, 100, math.pi, 40, energy=50, vision=0, wander_remaining=2)
    food = Food(100 + distance, 100)
    world.creatures = [creature]
    world.foods = [food]
    world.update(FIXED_DT)
    assert (food not in world.foods) == eaten
    assert creature.energy == pytest.approx(50 + (45 if eaten else 0) - 1.03 / 60)


def test_food_at_initial_position_is_consumed_before_moving_away():
    world = empty_world()
    creature = Creature(100, 100, 0, 40, energy=0.01, wander_remaining=3)
    world.creatures = [creature]
    food = Food(100, 100)
    world.foods = [food]
    world.update(0.5)
    assert creature in world.creatures
    assert creature.x == pytest.approx(120)
    assert world.foods == []
    assert creature.energy == pytest.approx(45.01 - 1.33 * 0.5)


def test_competing_creatures_cannot_eat_the_same_food_twice():
    world = empty_world()
    first = Creature(100, 100, 0, 40, energy=50, wander_remaining=3)
    second = Creature(100, 100, 0, 40, energy=50, wander_remaining=3)
    world.creatures = [first, second]
    world.foods = [Food(100, 100)]
    world.update(FIXED_DT)
    assert world.foods == []
    assert first.energy == pytest.approx(95 - 1.33 / 60)
    assert second.energy == pytest.approx(50 - 1.33 / 60)


def test_overlapping_food_units_are_each_consumed_once_and_energy_is_capped():
    world = empty_world()
    creature = Creature(100, 100, 0, 40, energy=100, wander_remaining=3)
    world.creatures = [creature]
    world.foods = [Food(100, 100), Food(100, 100)]
    world.update(FIXED_DT)
    assert world.foods == []
    assert creature.energy == pytest.approx(130 - 1.33 / 60)


def test_replenishment_preserves_fractional_seconds():
    world = empty_world()
    world.update(0.4)
    world.update(0.59)
    assert world.foods == []
    world.update(0.01)
    assert len(world.foods) == 1
    for _ in range(60):
        world.update(FIXED_DT)
    assert len(world.foods) == 2
    world.update(2.5)
    assert len(world.foods) == 4
    world.update(0.5)
    assert len(world.foods) == 5


def test_replenishment_does_not_round_a_genuinely_incomplete_second():
    world = empty_world()
    world.update(1 - 1e-10)
    assert world.foods == []
    world.update(1e-10)
    assert len(world.foods) == 1


def test_replenishment_caps_food_and_does_not_bank_credit_when_full():
    world = empty_world()
    world.update(1000)
    assert len(world.foods) == MAX_FOOD_COUNT
    world.update(1000)
    world.foods.pop()
    world.update(0.99)
    assert len(world.foods) == MAX_FOOD_COUNT - 1
    world.update(0.01)
    assert len(world.foods) == MAX_FOOD_COUNT
    assert all(
        FOOD_RADIUS <= food.x <= world.width - FOOD_RADIUS
        and FOOD_RADIUS <= food.y <= world.height - FOOD_RADIUS
        for food in world.foods
    )


def test_same_seed_and_fixed_steps_repeat_food_and_survival_state():
    first, second = World(seed=17), World(seed=17)
    for _ in range(600):
        first.update(FIXED_DT)
        second.update(FIXED_DT)
    assert first.creatures == second.creatures
    assert first.foods == second.foods
    assert first.random.getstate() == second.random.getstate()
