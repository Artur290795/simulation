"""
Модуль для главного абстрактного класса всех объектов на карте
"""

from abc import ABC

from core import Coordinates


class Entity(ABC):
    """
    Абстрактный корневой класс для всех объектов на карте.
    """

    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates
