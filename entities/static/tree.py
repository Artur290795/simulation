"""
Модуль для класса Tree
"""
from entities.base.entity import Entity
from core.coordinates import Coordinates


class Tree(Entity):
    """
    Статичный объект, препятствие
    """
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
