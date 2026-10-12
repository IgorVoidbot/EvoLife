"""Exemplos de movimento e reflexão especificados na Sprint 1."""

import math

import pytest

from evolife.config import CREATURE_RADIUS, WINDOW_HEIGHT, WINDOW_WIDTH
from evolife.creature import Creature


@pytest.mark.parametrize("dt, expected_x", [(0.0, 100.0), (0.5, 120.0), (1.0, 140.0)])
def test_eastward_displacement_from_prd(dt, expected_x):
    creature = Creature(x=100.0, y=100.0, direction=0.0, speed=40.0)
    creature.update(dt)
    assert creature.x == pytest.approx(expected_x)
    assert creature.y == pytest.approx(100.0)
    assert creature.energy == 100.0


@pytest.mark.parametrize("direction", [math.pi / 2, math.pi, -math.pi / 2, math.pi / 4])
def test_displacement_in_other_directions(direction):
    creature = Creature(400.0, 300.0, direction, 40.0)
    creature.update(0.5)
    assert creature.x == pytest.approx(400.0 + math.cos(direction) * 20)
    assert creature.y == pytest.approx(300.0 + math.sin(direction) * 20)


@pytest.mark.parametrize(
    "x, y, direction, expected_x, expected_y",
    [
        (790.0, 300.0, 0.0, 776.0, 300.0),
        (10.0, 300.0, math.pi, 24.0, 300.0),
        (400.0, 590.0, math.pi / 2, 400.0, 576.0),
        (400.0, 10.0, -math.pi / 2, 400.0, 24.0),
    ],
    ids=["direita", "esquerda", "inferior", "superior"],
)
def test_border_reflection_preserves_remaining_displacement(
    x, y, direction, expected_x, expected_y
):
    creature = Creature(x, y, direction, 40.0)
    creature.update(0.5)
    assert creature.x == pytest.approx(expected_x)
    assert creature.y == pytest.approx(expected_y)
    assert math.cos(creature.direction) == pytest.approx(-math.cos(direction))
    assert math.sin(creature.direction) == pytest.approx(-math.sin(direction))


def test_corner_reflects_both_axes():
    creature = Creature(790.0, 590.0, math.pi / 4, 40.0)
    creature.update(0.5)
    assert creature.x == pytest.approx(796.0 - 20 / math.sqrt(2))
    assert creature.y == pytest.approx(596.0 - 20 / math.sqrt(2))
    assert math.cos(creature.direction) < 0
    assert math.sin(creature.direction) < 0


def test_exact_contact_reflects_direction():
    creature = Creature(773.0, 300.0, 0.0, 40.0)
    creature.update(0.5)
    assert creature.x == WINDOW_WIDTH - CREATURE_RADIUS
    assert math.cos(creature.direction) == pytest.approx(-1.0)


def test_multiple_reflections_match_small_steps():
    single_step = Creature(400.0, 300.0, math.pi / 4, 90.0)
    many_steps = Creature(400.0, 300.0, math.pi / 4, 90.0)
    single_step.update(30.0)
    for _ in range(1800):
        many_steps.update(1 / 60)
    assert (single_step.x, single_step.y) == pytest.approx((many_steps.x, many_steps.y))
    assert single_step.direction == pytest.approx(many_steps.direction)
    assert CREATURE_RADIUS <= single_step.x <= WINDOW_WIDTH - CREATURE_RADIUS
    assert CREATURE_RADIUS <= single_step.y <= WINDOW_HEIGHT - CREATURE_RADIUS


@pytest.mark.parametrize("dt", [-1.0, float("inf"), float("nan")])
def test_invalid_elapsed_time_is_rejected(dt):
    creature = Creature(100.0, 100.0, 0.0, 40.0)
    with pytest.raises(ValueError, match="dt"):
        creature.update(dt)
