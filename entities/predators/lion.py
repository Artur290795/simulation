"""
Модуль для класса Lion
"""

from entities.predators.predator import Predator


class Lion(Predator):
    """Класс Лев, наследник хищного существа"""

    def __init__(self, coordinates, hp, speed, attack_power):
        super().__init__(coordinates, hp, speed, attack_power)
