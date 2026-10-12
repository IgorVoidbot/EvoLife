"""Estado e movimento da criatura, sem dependência de Pygame."""

from dataclasses import dataclass
import math
import random

from evolife.config import (
    BASE_ENERGY_COST,
    CREATURE_RADIUS,
    FOOD_ENERGY,
    INITIAL_EFFICIENCY,
    INITIAL_ENERGY,
    INITIAL_VISION,
    MAX_ENERGY,
    MAX_WANDER_INTERVAL,
    MIN_WANDER_INTERVAL,
    SPEED_ENERGY_COST,
    VISION_ENERGY_COST,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from evolife.food import Food


def _reflect_axis(
    position: float, velocity: float, lower: float, upper: float
) -> tuple[float, float]:
    """Espelhe o excesso de deslocamento, preservando a distância percorrida."""
    while position < lower or position > upper:
        if position < lower:
            position = 2 * lower - position
        else:
            position = 2 * upper - position
        velocity = -velocity

    # Também reflita quando o centro chega exatamente à borda, indo para fora.
    if (position == lower and velocity < 0) or (position == upper and velocity > 0):
        velocity = -velocity
    return position, velocity


@dataclass
class Creature:
    x: float
    y: float
    direction: float
    speed: float
    energy: float = INITIAL_ENERGY
    vision: float = INITIAL_VISION
    efficiency: float = INITIAL_EFFICIENCY
    wander_remaining: float = 0.0

    def steer(self, dt: float, foods: list[Food], rng: random.Random) -> None:
        """Persiga o alimento visível mais próximo ou mude a direção ao vagar."""
        target = None
        nearest_squared = self.vision**2
        for food in foods:
            distance_squared = (food.x - self.x) ** 2 + (food.y - self.y) ** 2
            if distance_squared <= nearest_squared and (
                target is None or distance_squared < nearest_squared
            ):
                target = food
                nearest_squared = distance_squared
        if target is not None:
            self.direction = math.atan2(target.y - self.y, target.x - self.x)
            return

        self.wander_remaining -= dt
        while self.wander_remaining <= 0:
            self.direction = rng.uniform(0.0, math.tau)
            self.wander_remaining += rng.uniform(
                MIN_WANDER_INTERVAL, MAX_WANDER_INTERVAL
            )

    def eat(self) -> None:
        """Receba a energia de uma unidade de comida, limitada ao teto."""
        self.energy = min(MAX_ENERGY, self.energy + FOOD_ENERGY)

    def spend_energy(self, dt: float) -> None:
        """Aplique o gasto por segundo do PRD, sem energia negativa."""
        cost = (
            BASE_ENERGY_COST
            + SPEED_ENERGY_COST * self.speed
            + VISION_ENERGY_COST * self.vision
        ) * self.efficiency
        self.energy = max(0.0, self.energy - cost * dt)

    def update(
        self,
        dt: float,
        width: float = WINDOW_WIDTH,
        height: float = WINDOW_HEIGHT,
        radius: float = CREATURE_RADIUS,
    ) -> None:
        """Avance em pixels por segundo e reflita nas bordas considerando o raio."""
        if not math.isfinite(dt) or dt < 0:
            raise ValueError("dt deve ser finito e não negativo")
        if radius < 0 or width <= 2 * radius or height <= 2 * radius:
            raise ValueError("o mundo deve comportar o diâmetro da criatura")
        if dt == 0:
            return

        velocity_x = math.cos(self.direction) * self.speed
        velocity_y = math.sin(self.direction) * self.speed
        self.x, reflected_x = _reflect_axis(
            self.x + velocity_x * dt, velocity_x, radius, width - radius
        )
        self.y, reflected_y = _reflect_axis(
            self.y + velocity_y * dt, velocity_y, radius, height - radius
        )
        if reflected_x != velocity_x or reflected_y != velocity_y:
            self.direction = math.atan2(reflected_y, reflected_x)
