"""
Определяет структуру для хранения координат клетки
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    """
    Неизменяемый dataclass с полями x, y.
    Используется как ключ в словаре карты и для передачи позиций.
    """

    x: int
    y: int
