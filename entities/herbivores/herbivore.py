"""
    Модуль для главного класса всех травоядных существ
"""
from __future__ import annotations
from entities.base.creature import Creature
from entities.base.entity import Entity
from entities.static.grass import Grass
from core.coordinates import Coordinates


class Herbivore(Creature):
    """
    Главный класс всех травоядных существ
    Описывает их основные характеристики:
    Цель – трава.
    При взаимодействии увеличивает HP на 2 (поедание).
    Не атакует, а поедает траву, при этом перемещается на её клетку.
    """
    def __init__(self, coordinates: Coordinates, hp: int, speed: int):
        super().__init__(coordinates, hp, speed)

    def get_target_class(self) -> Grass:
        return Grass

    def is_attack(self, target: Entity) -> bool:
        return isinstance(target, Grass)

    def interact_with_target(self, target: Grass) -> None:
        self.hp += 2
