"""Reprodução real, energia conservada, identidade e ciclo de vida da Sprint 3."""

import math
import random

import pytest

from evolife.config import CREATURE_RADIUS, FIXED_DT, OFFSPRING_DISTANCE
from evolife.creature import Creature
from evolife.world import World


def prepared_world(**parameters):
    world = World(seed=42, mutation_probability=0)
    state = dict(x=400, y=300, direction=0, speed=40, energy=120,
                 age_seconds=20, wander_remaining=3)
    state.update(parameters)
    parent = Creature(**state)
    world.creatures = [parent]
    world.foods.clear()
    return world, parent


@pytest.mark.parametrize(
    "age, energy, cooldown, expected",
    [(10, 110, 0, True), (9.999, 110, 0, False), (10, 109.999, 0, False),
     (10, 110, 0.001, False)],
    ids=["limites-inclusivos", "idade", "energia", "cooldown"],
)
def test_reproduction_requirements_are_inclusive(age, energy, cooldown, expected):
    creature = Creature(100, 100, 0, 40, energy=energy,
                        age_seconds=age, reproduction_cooldown=cooldown)
    assert creature.can_reproduce() is expected


@pytest.mark.parametrize(
    "parameters",
    [dict(age_seconds=2), dict(energy=50), dict(reproduction_cooldown=2)],
    ids=["idade-insuficiente", "energia-insuficiente", "cooldown-ativo"],
)
def test_world_blocks_birth_when_a_requirement_is_missing(parameters):
    world, parent = prepared_world(**parameters)
    world.update(FIXED_DT)
    assert world.creatures == [parent]
    assert world.births_total == 0


def test_birth_transfers_energy_and_defers_newborn_update():
    world, parent = prepared_world()
    previous_population = world.creatures
    world.update(FIXED_DT)
    assert previous_population == [parent]
    assert len(world.creatures) == 2
    child = world.creatures[1]
    assert parent.energy == pytest.approx(120 - 1.33 / 60 - 45)
    assert child.energy == 45
    assert parent.energy + child.energy == pytest.approx(120 - 1.33 / 60)
    assert parent.age_seconds == pytest.approx(20 + FIXED_DT)
    assert parent.reproduction_cooldown == 10
    assert child.age_seconds == 0
    assert child.reproduction_cooldown == 0
    assert world.births_total == 1
    assert world.deaths_total == 0
    world.update(FIXED_DT)
    assert child.age_seconds == FIXED_DT
    assert child.energy == pytest.approx(45 - 1.33 / 60)


def test_exact_energy_threshold_is_checked_after_metabolism():
    world, parent = prepared_world(energy=110)
    world.update(FIXED_DT)
    assert parent.energy < 110
    assert world.births_total == 0
    assert len(world.creatures) == 1


def test_age_reaches_ten_seconds_by_fixed_steps():
    world, parent = prepared_world(age_seconds=0, energy=130)
    for _ in range(599):
        world.foods.clear()
        world.update(FIXED_DT)
    assert parent.age_seconds < 10
    assert world.births_total == 0
    world.foods.clear()
    world.update(FIXED_DT)
    assert world.births_total == 1


def test_full_cooldown_prevents_repeated_birth_even_with_replenished_energy():
    world, parent = prepared_world()
    world.update(FIXED_DT)
    for _ in range(599):
        world.foods.clear()
        parent.energy = 130
        world.update(FIXED_DT)
    assert world.births_total == 1
    assert parent.reproduction_cooldown > 0
    parent.energy = 130
    world.foods.clear()
    world.update(FIXED_DT)
    assert world.births_total == 2
    assert parent.reproduction_cooldown == 10


def test_large_step_cannot_trigger_recursive_or_multiple_births():
    world, parent = prepared_world(energy=130)
    world.update(10)
    assert world.births_total == 1
    assert len(world.creatures) == 2
    assert world.creatures[1].age_seconds == 0
    assert world.creatures[1].energy == 45
    assert parent.reproduction_cooldown == 10


def test_child_copies_characteristics_and_increments_generation():
    world, parent = prepared_world(speed=88, vision=150, efficiency=0.8, generation=7)
    world.update(FIXED_DT)
    child = world.creatures[1]
    assert (child.speed, child.vision, child.efficiency) == (88, 150, 0.8)
    assert child.generation == 8
    assert parent.generation == 7
    assert isinstance(parent.id, int) and isinstance(child.id, int)
    assert child.id != parent.id
    child.speed = 25
    assert parent.speed == 88


@pytest.mark.parametrize(
    "x,y",
    [(7, 7), (793, 7), (7, 593), (793, 593),
     (7, 300), (793, 300), (400, 7), (400, 593)],
)
def test_child_is_near_parent_and_inside_every_border(x, y):
    world, parent = prepared_world(x=x, y=y)
    world.update(FIXED_DT)
    child = world.creatures[1]
    assert CREATURE_RADIUS <= child.x <= world.width - CREATURE_RADIUS
    assert CREATURE_RADIUS <= child.y <= world.height - CREATURE_RADIUS
    assert math.dist((parent.x, parent.y), (child.x, child.y)) <= OFFSPRING_DISTANCE + 1e-12


def test_birth_fits_a_small_valid_world():
    world = World(width=20, height=20)
    world.foods.clear()
    world.creatures = [Creature(10, 10, 0, 40, energy=120, age_seconds=20)]
    world.update(FIXED_DT)
    child = world.creatures[1]
    assert 7 <= child.x <= 13
    assert 7 <= child.y <= 13


def test_initial_ids_and_generations_and_zero_event_counts():
    world = World()
    assert [creature.id for creature in world.creatures] == list(range(10))
    assert all(creature.generation == 0 and creature.age_seconds == 0
               for creature in world.creatures)
    assert world.births_total == world.deaths_total == 0


def test_ids_are_not_reused_after_deaths():
    world = World()
    original_ids = {creature.id for creature in world.creatures}
    parent = world.creatures[0]
    parent.energy, parent.age_seconds = 120, 20
    for creature in world.creatures[1:]:
        creature.energy = 0
    world.foods.clear()
    world.update(FIXED_DT)
    first_child = world.creatures[1]
    assert first_child.id not in original_ids
    first_child.energy = 0
    parent.energy, parent.reproduction_cooldown = 120, 0
    world.update(FIXED_DT)
    second_child = world.creatures[1]
    assert second_child.id not in original_ids | {first_child.id}
    assert second_child.id > first_child.id
    assert world.births_total == 2
    assert world.deaths_total == 10


def test_simultaneous_births_and_deaths_preserve_iteration_and_count_once():
    world, first = prepared_world()
    second = Creature(200, 200, 0, 40, energy=120, age_seconds=20)
    dead_before = Creature(100, 100, 0, 40, energy=0)
    dying = Creature(150, 150, 0, 40, energy=0.001, age_seconds=20)
    world.creatures = [dead_before, first, dying, second]
    old_population = world.creatures
    world.update(FIXED_DT)
    assert old_population == [dead_before, first, dying, second]
    assert world.creatures[:2] == [first, second]
    assert len(world.creatures) == 4
    assert len({creature.id for creature in world.creatures}) == 4
    assert all(child.age_seconds == 0 for child in world.creatures[2:])
    assert world.births_total == world.deaths_total == 2
    world.update(FIXED_DT)
    assert world.births_total == world.deaths_total == 2


def test_extinction_continues_without_repeated_death_counts():
    world, parent = prepared_world(energy=0.001)
    world.update(FIXED_DT)
    frozen_state = vars(parent).copy()
    for _ in range(600):
        world.update(FIXED_DT)
    assert world.creatures == []
    assert world.births_total == 0
    assert world.deaths_total == 1
    assert len(world.foods) == 10
    assert vars(parent) == frozen_state


def test_zero_step_does_not_trigger_birth_or_lifecycle_changes():
    world, parent = prepared_world()
    previous = vars(parent).copy()
    rng = world.random.getstate()
    world.update(0)
    assert vars(parent) == previous
    assert world.births_total == world.deaths_total == 0
    assert world.random.getstate() == rng


def test_same_seed_repeats_births_deaths_ids_and_state():
    global_state = random.getstate()
    first, second = World(seed=42), World(seed=42)
    for _ in range(3600):
        first.update(FIXED_DT)
        second.update(FIXED_DT)
    assert first.births_total > 0
    assert first.deaths_total > 0
    assert first.creatures == second.creatures
    assert first.foods == second.foods
    assert (first.births_total, first.deaths_total) == (second.births_total, second.deaths_total)
    assert first.random.getstate() == second.random.getstate()
    assert random.getstate() == global_state
