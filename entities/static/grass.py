"""
Модуль для класса Grass(Трава)
"""

from entities.base.entity import Entity
from core.coordinates import Coordinates


class Grass(Entity):
    """
    Статичный объект, ресурс для травоядных
    """

    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
