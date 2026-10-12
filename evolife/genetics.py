"""Genes herdáveis e mutações aleatórias limitadas, sem Pygame."""

from dataclasses import dataclass
import math
import random

from evolife.config import (
    INITIAL_EFFICIENCY,
    INITIAL_VISION,
    MAX_EFFICIENCY,
    MAX_SPEED,
    MAX_VISION,
    MIN_EFFICIENCY,
    MIN_SPEED,
    MIN_VISION,
    MUTATION_PROBABILITY,
    MUTATION_STDDEV_FRACTION,
)


GENE_RANGES = (
    ("speed", MIN_SPEED, MAX_SPEED),
    ("vision", MIN_VISION, MAX_VISION),
    ("efficiency", MIN_EFFICIENCY, MAX_EFFICIENCY),
)


def _validate_number(name: str, value: float, lower: float, upper: float) -> None:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
        or not lower <= value <= upper
    ):
        raise ValueError(f"{name} deve ser finito e estar entre {lower} e {upper}")


@dataclass(frozen=True)
class MutationSettings:
    probability: float = MUTATION_PROBABILITY
    stddev_fraction: float = MUTATION_STDDEV_FRACTION

    def __post_init__(self) -> None:
        _validate_number("probability", self.probability, 0.0, 1.0)
        _validate_number("stddev_fraction", self.stddev_fraction, 0.0, math.inf)


@dataclass(frozen=True)
class Genes:
    speed: float
    vision: float = INITIAL_VISION
    efficiency: float = INITIAL_EFFICIENCY

    def __post_init__(self) -> None:
        for name, lower, upper in GENE_RANGES:
            _validate_number(name, getattr(self, name), lower, upper)

    def inherit(
        self, rng: random.Random, settings: MutationSettings = MutationSettings()
    ) -> "Genes":
        """Copie os genes; sorteie cada mutação e limite a variação normal."""
        values = {}
        for name, lower, upper in GENE_RANGES:
            value = getattr(self, name)
            if rng.random() < settings.probability:
                value += rng.gauss(0.0, settings.stddev_fraction * (upper - lower))
                value = min(upper, max(lower, value))
            values[name] = value
        return Genes(**values)
