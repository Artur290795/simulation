"""
Модуль для класса Hyena
"""

from entities.predators.predator import Predator


class Hyena(Predator):
    """Класс Гиена, наследник хищного существа"""

    def __init__(self, coordinates, hp, speed, attack_power):
        super().__init__(coordinates, hp, speed, attack_power)
