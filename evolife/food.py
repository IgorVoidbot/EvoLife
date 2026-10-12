"""Posição de uma unidade de alimento, sem dependência de Pygame."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Food:
    x: float
    y: float
