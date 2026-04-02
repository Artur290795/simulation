"""
Модуль для класса Zebra
"""
from entities.herbivores.herbivore import Herbivore


class Zebra(Herbivore):
    """Класс Зебр, наследник травоядного"""
    def __init__(self, coordinates, hp, speed):
        super().__init__(coordinates, hp, speed)