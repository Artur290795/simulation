"""
Модуль для главного класса всех хищных существ
"""

from __future__ import annotations
from entities.base.creature import Creature
from entities.base.entity import Entity
from entities.herbivores.herbivore import Herbivore
from core.coordinates import Coordinates


class Predator(Creature):
    """
    Главный класс всех хищных] существ
    Описывает их основные характеристики:
    Цель – травоядное существо.
    При взаимодействии увеличивает HP жертвы на attach_pwoer.
    При смерти жертвы перемещается на её клетку.
    """

    def __init__(
        self, coordinates: Coordinates, hp: int, speed: int, attack_power: int
    ):
        super().__init__(coordinates, hp, speed)
        self.attack_power = attack_power

    def get_target_class(self) -> Herbivore:
        return Herbivore

    def is_attack(self, target: Entity) -> bool:
        return isinstance(target, Herbivore)

    def interact_with_target(self, target: Herbivore) -> None:
        target.hp -= self.attack_power
