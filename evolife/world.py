"""Movimento, sobrevivência e reprodução, independentes de Pygame."""

import math
import random

from evolife.config import (
    CREATURE_RADIUS,
    DEFAULT_SEED,
    FOOD_RADIUS,
    FOOD_SPAWN_RATE,
    INITIAL_FOOD_COUNT,
    INITIAL_POPULATION,
    MAX_FOOD_COUNT,
    MAX_SPEED,
    MAX_WANDER_INTERVAL,
    MIN_SPEED,
    MIN_WANDER_INTERVAL,
    OFFSPRING_DISTANCE,
    REPRODUCTION_COOLDOWN,
    REPRODUCTION_ENERGY_TRANSFER,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from evolife.creature import Creature
from evolife.food import Food


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
        self._next_creature_id = 0
        self.births_total = 0
        self.deaths_total = 0
        self.creatures = [
            Creature(
                x=self.random.uniform(CREATURE_RADIUS, width - CREATURE_RADIUS),
                y=self.random.uniform(CREATURE_RADIUS, height - CREATURE_RADIUS),
                direction=self.random.uniform(0.0, math.tau),
                speed=self.random.uniform(MIN_SPEED, MAX_SPEED),
                id=self._allocate_id(),
            )
            for _ in range(INITIAL_POPULATION)
        ]
        for creature in self.creatures:
            creature.wander_remaining = self.random.uniform(
                MIN_WANDER_INTERVAL, MAX_WANDER_INTERVAL
            )
        self.foods = [self._create_food() for _ in range(INITIAL_FOOD_COUNT)]
        self._food_spawn_progress = 0.0

    def _allocate_id(self) -> int:
        creature_id = self._next_creature_id
        self._next_creature_id += 1
        return creature_id

    def _reproduce(self, parent: Creature) -> Creature:
        """Crie um filhote próximo e transfira energia, sem atualizar a população."""
        angle = self.random.uniform(0.0, math.tau)
        child = Creature(
            x=min(
                self.width - CREATURE_RADIUS,
                max(CREATURE_RADIUS, parent.x + math.cos(angle) * OFFSPRING_DISTANCE),
            ),
            y=min(
                self.height - CREATURE_RADIUS,
                max(CREATURE_RADIUS, parent.y + math.sin(angle) * OFFSPRING_DISTANCE),
            ),
            direction=angle,
            speed=parent.speed,
            energy=REPRODUCTION_ENERGY_TRANSFER,
            vision=parent.vision,
            efficiency=parent.efficiency,
            wander_remaining=self.random.uniform(
                MIN_WANDER_INTERVAL, MAX_WANDER_INTERVAL
            ),
            id=self._allocate_id(),
            generation=parent.generation + 1,
        )
        parent.energy -= REPRODUCTION_ENERGY_TRANSFER
        parent.reproduction_cooldown = REPRODUCTION_COOLDOWN
        return child

    def _create_food(self) -> Food:
        return Food(
            self.random.uniform(FOOD_RADIUS, self.width - FOOD_RADIUS),
            self.random.uniform(FOOD_RADIUS, self.height - FOOD_RADIUS),
        )

    def _consume_food(self, creature: Creature) -> None:
        """Cada alimento em contato é consumido uma vez, em ordem da população."""
        remaining = []
        collision_squared = (CREATURE_RADIUS + FOOD_RADIUS) ** 2
        for food in self.foods:
            distance_squared = (food.x - creature.x) ** 2 + (food.y - creature.y) ** 2
            if distance_squared <= collision_squared:
                creature.eat()
            else:
                remaining.append(food)
        self.foods = remaining

    def _replenish_food(self, dt: float) -> None:
        """Acumule frações de unidade; descarte crédito quando o mapa está cheio."""
        if len(self.foods) >= MAX_FOOD_COUNT:
            self._food_spawn_progress = 0.0
            return
        self._food_spawn_progress += FOOD_SPAWN_RATE * dt
        units = math.floor(self._food_spawn_progress)
        if math.isclose(
            self._food_spawn_progress, units + 1, rel_tol=0.0, abs_tol=1e-12
        ):
            units += 1
        self._food_spawn_progress = max(0.0, self._food_spawn_progress - units)
        for _ in range(min(units, MAX_FOOD_COUNT - len(self.foods))):
            self.foods.append(self._create_food())
        if len(self.foods) == MAX_FOOD_COUNT:
            self._food_spawn_progress = 0.0

    def update(self, dt: float) -> None:
        """Avance sobrevivência e reprodução; aplique mortes e nascimentos ao final."""
        if not math.isfinite(dt) or dt < 0:
            raise ValueError("dt deve ser finito e não negativo")
        if dt == 0:
            return

        survivors = []
        newborns = []
        for creature in self.creatures:
            # Criaturas de cenários preparados também recebem ID do mundo.
            if creature.id is None:
                creature.id = self._allocate_id()
            if creature.energy <= 0:
                self.deaths_total += 1
                continue
            creature.advance_lifecycle(dt)
            # Comida na posição inicial também conta, antes de sair do contato.
            self._consume_food(creature)
            creature.steer(dt, self.foods, self.random)
            creature.update(dt, self.width, self.height)
            self._consume_food(creature)
            creature.spend_energy(dt)
            if creature.energy > 0:
                survivors.append(creature)
                if creature.can_reproduce():
                    newborns.append(self._reproduce(creature))
            else:
                self.deaths_total += 1
        self.creatures = survivors + newborns
        self.births_total += len(newborns)
        self._replenish_food(dt)
