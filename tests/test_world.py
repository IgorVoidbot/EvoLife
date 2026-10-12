"""População, limites e independência do domínio."""

import random
import subprocess
import sys

import pytest

from evolife.config import CREATURE_RADIUS, FIXED_DT, MAX_SPEED, MIN_SPEED
from evolife.world import World


def test_initial_population_has_ten_distinct_positions_and_directions():
    global_random_state = random.getstate()
    world = World()
    assert len(world.creatures) == 10
    assert len({(creature.x, creature.y) for creature in world.creatures}) == 10
    assert len({creature.direction for creature in world.creatures}) == 10
    assert random.getstate() == global_random_state
    for creature in world.creatures:
        assert CREATURE_RADIUS <= creature.x <= world.width - CREATURE_RADIUS
        assert CREATURE_RADIUS <= creature.y <= world.height - CREATURE_RADIUS
        assert MIN_SPEED <= creature.speed <= MAX_SPEED
        assert creature.energy == 100.0


def test_all_creatures_move_and_stay_inside_for_one_minute():
    world = World()
    initial_positions = [(creature.x, creature.y) for creature in world.creatures]
    for _ in range(3600):
        world.update(FIXED_DT)
        for creature in world.creatures:
            assert CREATURE_RADIUS <= creature.x <= world.width - CREATURE_RADIUS
            assert CREATURE_RADIUS <= creature.y <= world.height - CREATURE_RADIUS
    assert len(world.creatures) == 10
    for creature, initial in zip(world.creatures, initial_positions):
        assert (creature.x, creature.y) != pytest.approx(initial)
        assert 0 < creature.energy <= 130.0


def test_empty_world_remains_updatable():
    world = World()
    world.creatures.clear()
    world.update(FIXED_DT)
    assert world.creatures == []


def test_domain_imports_without_pygame():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import evolife.creature, evolife.world, evolife.food, sys; "
            "assert 'pygame' not in sys.modules",
        ],
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stdout + result.stderr
