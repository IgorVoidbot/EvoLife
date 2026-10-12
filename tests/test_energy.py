"""Fórmula de energia, teto, morte e extinção sem reprodução."""

import pytest

from evolife.config import FIXED_DT
from evolife.creature import Creature
from evolife.food import Food
from evolife.world import World


@pytest.mark.parametrize(
    "speed, vision, efficiency, expected_cost",
    [(40, 100, 1, 1.33), (25, 35, 0.8, 0.764), (90, 160, 1.2, 2.532)],
)
def test_energy_follows_prd_formula(speed, vision, efficiency, expected_cost):
    creature = Creature(100, 100, 0, speed, vision=vision, efficiency=efficiency)
    creature.spend_energy(0.5)
    assert creature.energy == pytest.approx(100 - expected_cost * 0.5)


@pytest.mark.parametrize("initial, expected", [(50, 95), (100, 130), (129, 130)])
def test_food_energy_gain_and_cap(initial, expected):
    creature = Creature(100, 100, 0, 40, energy=initial)
    creature.eat()
    assert creature.energy == expected


def test_energy_is_clamped_at_zero():
    creature = Creature(100, 100, 0, 40, energy=0.01)
    creature.spend_energy(1)
    assert creature.energy == 0


def test_all_simultaneous_deaths_are_removed_without_skipping_survivor():
    world = World()
    world.foods.clear()
    dead = [Creature(100, 100, 0, 40, energy=0.01) for _ in range(3)]
    survivor = Creature(300, 300, 0, 40, wander_remaining=3)
    world.creatures = [dead[0], survivor, dead[1], dead[2]]
    world.update(FIXED_DT)
    assert world.creatures == [survivor]
    assert all(creature.energy == 0 for creature in dead)
    positions = [(creature.x, creature.y) for creature in dead]
    world.update(FIXED_DT)
    assert [(creature.x, creature.y) for creature in dead] == positions
    assert survivor.energy == pytest.approx(100 - 1.33 * 2 / 60)


def test_already_dead_creature_does_not_move_or_consume_food():
    world = World()
    creature = Creature(100, 100, 0, 40, energy=0)
    world.creatures = [creature]
    world.foods = [Food(100, 100)]
    world.update(FIXED_DT)
    assert world.creatures == []
    assert (creature.x, creature.y, creature.energy) == (100, 100, 0)
    assert world.foods == [Food(100, 100)]


def test_exact_zero_energy_removes_creature():
    world = World()
    world.creatures = [Creature(100, 100, 0, 40, energy=1.33, wander_remaining=3)]
    world.foods.clear()
    world.update(1)
    assert world.creatures == []


def test_world_keeps_replenishing_after_extinction():
    world = World()
    world.creatures = [Creature(100, 100, 0, 40, energy=0.001)]
    world.foods.clear()
    for _ in range(600):
        world.update(FIXED_DT)
    assert world.creatures == []
    assert len(world.foods) == 10


@pytest.mark.parametrize("dt", [-1, float("nan"), float("inf")])
@pytest.mark.parametrize("populated", [True, False])
def test_invalid_dt_is_rejected_even_after_extinction(dt, populated):
    world = World()
    if not populated:
        world.creatures.clear()
    creatures = [vars(creature).copy() for creature in world.creatures]
    foods = world.foods.copy()
    state = world.random.getstate()
    with pytest.raises(ValueError, match="dt"):
        world.update(dt)
    assert [vars(creature) for creature in world.creatures] == creatures
    assert world.foods == foods
    assert world.random.getstate() == state


def test_zero_dt_does_not_change_state_or_randomness():
    world = World()
    world.foods = [Food(world.creatures[0].x, world.creatures[0].y)]
    creatures = [vars(creature).copy() for creature in world.creatures]
    foods = world.foods.copy()
    state = world.random.getstate()
    world.update(0)
    assert [vars(creature) for creature in world.creatures] == creatures
    assert world.foods == foods
    assert world.random.getstate() == state
