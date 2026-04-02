"""
Модуль для класса Giraffe
"""
from entities.herbivores.herbivore import Herbivore


class Giraffe(Herbivore):
    """Класс Жирафов, наследник травоядного"""
    def __init__(self, coordinates, hp, speed):
        super().__init__(coordinates, hp, speed)