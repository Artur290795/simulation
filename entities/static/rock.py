"""
Модуль для класса Rock
"""
from entities.base.entity import Entity
from core.coordinates import Coordinates


class Rock(Entity):
    """
    Статичный объект, препятствие
    """
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)