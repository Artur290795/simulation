"""
Модуль для класса Antelope
"""
from entities.herbivores.herbivore import Herbivore


class Antelope(Herbivore):
    """Класс Антилопы, наследник травоядного"""
    def __init__(self, coordinates, hp, speed):
        super().__init__(coordinates, hp, speed)