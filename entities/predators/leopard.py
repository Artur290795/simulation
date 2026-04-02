"""
Модуль для класса Leopard
"""

from entities.predators.predator import Predator


class Leopard(Predator):
    """Класс Леопард, наследник хищного существа"""

    def __init__(self, coordinates, hp, speed, attack_power):
        super().__init__(coordinates, hp, speed, attack_power)
