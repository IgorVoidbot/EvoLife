"""Herança, sorteios controlados, limites e integração genética da Sprint 4."""

from dataclasses import FrozenInstanceError, replace
import itertools
import math
import random
from unittest.mock import Mock

import pytest

from evolife.config import FIXED_DT
from evolife.creature import Creature
from evolife.food import Food
from evolife.genetics import GENE_RANGES, Genes, MutationSettings
from evolife.world import World


def controlled_rng(draws, changes=()):
    rng = Mock(spec=random.Random)
    rng.random.side_effect = draws
    rng.gauss.side_effect = changes
    return rng


def birth_world(**settings):
    world = World(seed=42, **settings)
    parent = Creature(400, 300, 0, genes=Genes(40, 100, 1),
                      energy=120, age_seconds=20, wander_remaining=3)
    world.creatures = [parent]
    world.foods.clear()
    return world, parent


def test_inheritance_without_mutation_is_equal_and_independent():
    parent = Genes(40, 100, 1)
    rng = controlled_rng([0, 0.5, 0.999])
    child = parent.inherit(rng, MutationSettings(probability=0))
    assert child == parent
    assert child is not parent
    assert rng.random.call_count == 3
    rng.gauss.assert_not_called()
    with pytest.raises(FrozenInstanceError):
        child.speed = 50
    assert parent.speed == 40


@pytest.mark.parametrize("mask", list(itertools.product([False, True], repeat=3)))
def test_mutation_is_independent_for_each_gene(mask):
    parent = Genes(50, 100, 1)
    rng = controlled_rng([0.119 if mutate else 0.12 for mutate in mask],
                         [0.01] * sum(mask))
    child = parent.inherit(rng)
    assert rng.random.call_count == 3
    expected_sigmas = [5.2, 10, 0.032]
    expected_calls = []
    for (name, _, _), mutate, sigma in zip(GENE_RANGES, mask, expected_sigmas):
        assert getattr(child, name) == pytest.approx(
            getattr(parent, name) + (0.01 if mutate else 0)
        )
        if mutate:
            expected_calls.append((0, sigma))
    assert len(rng.gauss.call_args_list) == sum(mask)
    for call, expected in zip(rng.gauss.call_args_list, expected_calls):
        assert call.args == pytest.approx(expected)


@pytest.mark.parametrize("probability, draw, mutated", [
    (0, 0, False), (0.12, 0.119999, True), (0.12, 0.12, False),
    (0.5, 0.49, True), (0.5, 0.5, False), (1, 0.999999, True),
])
def test_configurable_probability_uses_strict_threshold(probability, draw, mutated):
    parent = Genes(50, 100, 1)
    rng = controlled_rng([draw] * 3, [0.01] * 3)
    child = parent.inherit(rng, MutationSettings(probability=probability))
    assert (child != parent) is mutated
    assert rng.gauss.call_count == (3 if mutated else 0)


@pytest.mark.parametrize("fraction", [0, 0.04, 0.08, 0.2])
def test_configurable_normal_deviation_uses_each_gene_amplitude(fraction):
    rng = controlled_rng([0] * 3, [0] * 3)
    parent = Genes(50, 100, 1)
    assert parent.inherit(rng, MutationSettings(1, fraction)) == parent
    for call, (_, lower, upper) in zip(rng.gauss.call_args_list, GENE_RANGES):
        assert call.args == pytest.approx((0, fraction * (upper - lower)))


@pytest.mark.parametrize("name, lower, upper", GENE_RANGES)
@pytest.mark.parametrize("at_upper", [False, True])
@pytest.mark.parametrize("near", [False, True])
def test_outward_mutations_at_or_near_limits_are_clamped(name, lower, upper, at_upper, near):
    edge = upper if at_upper else lower
    offset = (upper - lower) * 0.001 if near else 0
    initial = edge - offset if at_upper else edge + offset
    parent = replace(Genes(50, 100, 1), **{name: initial})
    draws = [0 if gene == name else 0.9 for gene, _, _ in GENE_RANGES]
    rng = controlled_rng(draws, [2 * (upper - lower) * (1 if at_upper else -1)])
    child = parent.inherit(rng)
    assert getattr(child, name) == edge
    assert getattr(parent, name) == initial
    for gene, minimum, maximum in GENE_RANGES:
        assert minimum <= getattr(child, gene) <= maximum


@pytest.mark.parametrize("name, lower, upper", GENE_RANGES)
@pytest.mark.parametrize("at_upper", [False, True])
def test_mutations_can_move_inward_from_both_limits(name, lower, upper, at_upper):
    parent = replace(Genes(50, 100, 1), **{name: upper if at_upper else lower})
    change = (upper - lower) * (0.01 if not at_upper else -0.01)
    rng = controlled_rng([0 if gene == name else 0.9 for gene, _, _ in GENE_RANGES],
                         [change])
    child = parent.inherit(rng)
    assert getattr(child, name) == pytest.approx(getattr(parent, name) + change)
    assert lower < getattr(child, name) < upper


@pytest.mark.parametrize("change", [-0.01, 0, 0.01])
def test_mutations_allow_negative_zero_and_positive_changes(change):
    parent = Genes(50, 100, 1)
    child = parent.inherit(controlled_rng([0] * 3, [change] * 3))
    assert child == Genes(50 + change, 100 + change, 1 + change)


@pytest.mark.parametrize("name, lower, upper", GENE_RANGES)
@pytest.mark.parametrize("invalid", ["below", "above", float("nan"),
                                     float("inf"), float("-inf"), True, "40", None])
def test_invalid_genetic_values_are_rejected(name, lower, upper, invalid):
    if invalid == "below":
        invalid = lower - 0.001
    elif invalid == "above":
        invalid = upper + 0.001
    with pytest.raises(ValueError, match=name):
        replace(Genes(50, 100, 1), **{name: invalid})


@pytest.mark.parametrize("values", [(25, 35, 0.8), (90, 160, 1.2)])
def test_gene_limits_are_inclusive(values):
    assert Genes(*values) == Genes(*values)


@pytest.mark.parametrize("invalid", [-0.01, 1.01, float("nan"), float("inf"), True, "0.12"])
def test_invalid_mutation_probability_is_rejected(invalid):
    with pytest.raises(ValueError, match="probability"):
        MutationSettings(probability=invalid)
    with pytest.raises(ValueError, match="probability"):
        World(mutation_probability=invalid)


@pytest.mark.parametrize("invalid", [-0.01, float("nan"), float("inf"), True, "0.08"])
def test_invalid_mutation_deviation_is_rejected(invalid):
    with pytest.raises(ValueError, match="stddev_fraction"):
        MutationSettings(stddev_fraction=invalid)
    with pytest.raises(ValueError, match="stddev_fraction"):
        World(mutation_stddev_fraction=invalid)


@pytest.mark.parametrize("name, lower, upper", GENE_RANGES)
def test_legacy_properties_share_validated_genes_without_changing_other_creatures(name, lower, upper):
    genes = Genes(50, 100, 1)
    first = Creature(100, 100, 0, genes=genes)
    second = Creature(200, 200, 0, genes=genes)
    setattr(first, name, upper)
    assert getattr(first.genes, name) == upper
    assert second.genes == genes
    before = first.genes
    with pytest.raises(ValueError, match=name):
        setattr(first, name, lower - 0.01)
    assert first.genes is before


def test_creature_accepts_old_constructor_and_rejects_conflicting_genes():
    creature = Creature(100, 100, 0, 40, 90, 75, 0.9)
    assert creature.genes == Genes(40, 75, 0.9)
    assert creature.energy == 90
    with pytest.raises(ValueError, match="separadamente"):
        Creature(100, 100, 0, 40, genes=Genes(50))
    with pytest.raises(ValueError, match="speed ou genes"):
        Creature(100, 100, 0)
    with pytest.raises(TypeError, match="Genes"):
        creature.genes = (40, 75, 0.9)
    assert creature.genes == Genes(40, 75, 0.9)


@pytest.mark.parametrize("probability", [0, 1])
def test_world_birth_uses_its_mutation_settings_and_conserves_energy(probability, monkeypatch):
    world, parent = birth_world(mutation_probability=probability)
    original_genes = parent.genes
    monkeypatch.setattr(world.random, "gauss", lambda mean, sigma: sigma)
    world.update(FIXED_DT)
    child = world.creatures[1]
    assert child.genes == (Genes(45.2, 110, 1.032) if probability else original_genes)
    assert parent.genes is original_genes
    assert child.genes is not original_genes
    assert child.parent_id == parent.id
    assert child.id != parent.id
    assert child.generation == parent.generation + 1
    assert parent.parent_id is None
    assert child.energy == 45
    assert parent.energy + child.energy == pytest.approx(120 - 1.33 * FIXED_DT)
    assert parent.reproduction_cooldown == 10
    assert child.age_seconds == child.reproduction_cooldown == 0
    start = (child.x, child.y)
    world.update(FIXED_DT)
    assert child.age_seconds == FIXED_DT
    assert (child.x, child.y) != start
    cost = (0.55 + 0.012 * child.speed + 0.003 * child.vision) * child.efficiency
    assert child.energy == pytest.approx(45 - cost * FIXED_DT)


def test_two_descendant_generations_inherit_and_trace_parents_with_official_rules():
    world, parent = birth_world(mutation_probability=0)
    world.update(FIXED_DT)
    child = world.creatures[1]
    # Apenas alimento preparado; idade, cooldown e energia seguem as regras reais.
    for _ in range(600):
        world.foods = [Food(child.x, child.y)]
        world.update(FIXED_DT)
    grandchildren = [creature for creature in world.creatures if creature.parent_id == child.id]
    assert len(grandchildren) == 1
    grandchild = grandchildren[0]
    assert (parent.generation, child.generation, grandchild.generation) == (0, 1, 2)
    assert child.parent_id == parent.id
    assert grandchild.parent_id == child.id
    assert len({parent.id, child.id, grandchild.id}) == 3
    assert parent.genes == child.genes == grandchild.genes
    assert child.age_seconds >= 10
    assert child.reproduction_cooldown == 10
    assert grandchild.energy == 45
    assert grandchild.age_seconds == 0


def test_mutated_genes_affect_movement_perception_and_energy_cost():
    parent_genes = Genes(40, 100, 1)
    child_genes = parent_genes.inherit(controlled_rng([0] * 3, [5.2, 10, 0.032]))
    parent = Creature(300, 300, math.pi, genes=parent_genes, wander_remaining=3)
    child = Creature(300, 300, math.pi, genes=child_genes, wander_remaining=3)
    foods = [Food(405, 300)]
    parent.steer(FIXED_DT, foods, random.Random(42))
    child.steer(FIXED_DT, foods, random.Random(42))
    assert parent.direction == math.pi
    assert child.direction == 0
    child.update(FIXED_DT)
    assert child.x == pytest.approx(300 + child_genes.speed * FIXED_DT)
    parent.spend_energy(1)
    child.spend_energy(1)
    assert parent.energy == pytest.approx(100 - 1.33)
    assert child.energy == pytest.approx(100 - (0.55 + 0.012 * 45.2 + 0.003 * 110) * 1.032)
    assert child.energy < parent.energy


@pytest.mark.parametrize("probability", [0, 0.12, 1])
def test_seed_and_fixed_steps_repeat_genetics_and_lineage(probability):
    global_state = random.getstate()
    first = World(seed=17, mutation_probability=probability)
    second = World(seed=17, mutation_probability=probability)
    for _ in range(1800):
        first.update(FIXED_DT)
        second.update(FIXED_DT)
    assert first.births_total > 0
    assert first.creatures == second.creatures
    assert first.foods == second.foods
    assert (first.births_total, first.deaths_total) == (second.births_total, second.deaths_total)
    assert first.random.getstate() == second.random.getstate()
    assert random.getstate() == global_state
    for creature in first.creatures:
        for name, lower, upper in GENE_RANGES:
            assert lower <= getattr(creature.genes, name) <= upper
        if creature.generation:
            assert creature.parent_id is not None


def test_mutation_enabled_world_continues_after_extinction():
    world = World(mutation_probability=1)
    world.creatures.clear()
    world.foods.clear()
    for _ in range(600):
        world.update(FIXED_DT)
    assert world.creatures == []
    assert world.births_total == world.deaths_total == 0
    assert len(world.foods) == 10
