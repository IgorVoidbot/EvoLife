"""Estado e movimento da criatura, sem dependência de Pygame."""

from dataclasses import dataclass
import math

from evolife.config import CREATURE_RADIUS, INITIAL_ENERGY, WINDOW_HEIGHT, WINDOW_WIDTH


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
