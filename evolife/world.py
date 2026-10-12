"""População inicial e atualização do mundo, independentes de Pygame."""

import math
import random

from evolife.config import (
    CREATURE_RADIUS,
    DEFAULT_SEED,
    INITIAL_POPULATION,
    MAX_SPEED,
    MIN_SPEED,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from evolife.creature import Creature


class World:
    def __init__(
        self,
        width: float = WINDOW_WIDTH,
        height: float = WINDOW_HEIGHT,
        seed: int | None = DEFAULT_SEED,
    ) -> None:
        if width <= 2 * CREATURE_RADIUS or height <= 2 * CREATURE_RADIUS:
            raise ValueError("o mundo deve comportar o diâmetro da criatura")
        self.width = width
        self.height = height
        self.random = random.Random(seed)
        self.creatures = [
            Creature(
                x=self.random.uniform(CREATURE_RADIUS, width - CREATURE_RADIUS),
                y=self.random.uniform(CREATURE_RADIUS, height - CREATURE_RADIUS),
                direction=self.random.uniform(0.0, math.tau),
                speed=self.random.uniform(MIN_SPEED, MAX_SPEED),
            )
            for _ in range(INITIAL_POPULATION)
        ]

    def update(self, dt: float) -> None:
        """Avance todas as criaturas sem desenhar ou alterar a população."""
        for creature in self.creatures:
            creature.update(dt, self.width, self.height)
