"""
Модуль для фабрики создания сущностей
"""

from __future__ import annotations
from random import randint, choice
from entities.static import Grass, Rock, Tree
from entities.herbivores import Antelope, Giraffe, Herbivore, Zebra
from entities.predators import Hyena, Leopard, Lion, Predator
from core import Coordinates


class EntityFactory:
    """
    Фабрика для содания сущностей

    create_entities(amount, entity_class) –
        создаёт указанное количество сущностей случайным образом на свободные клетки.

    create() – создаёт полный набор объектов в количествах, заданных при инициализации.

    класс имеет методы для создания каждого из видом сущностей
    """

    PREDATORS = [Lion, Leopard, Hyena]
    HERBIVORES = [Antelope, Giraffe, Zebra]

    def __init__(self, game_map: "Map", predators_amount: int, herbivores_amount: int):
        self.game_map = game_map
        self.predators_amount = predators_amount
        self.herbivores_amount = herbivores_amount
        self.grasses_amount = int(herbivores_amount * 2.5)
        self.rocks_amount = (predators_amount + herbivores_amount) // 2
        self.trees_amount = (predators_amount + herbivores_amount) // 2

    def create(self):
        self.create_entities(self.predators_amount, Predator)
        self.create_entities(self.herbivores_amount, Herbivore)
        self.create_entities(self.grasses_amount, Grass)
        self.create_entities(self.rocks_amount, Rock)
        self.create_entities(self.trees_amount, Tree)

    def create_entities(self, entities_amount: int, entity: type):
        entities_createed = 0
        while entities_createed < entities_amount:
            new_coord = self._get_random_coordinates()
            if self.game_map.is_empty_cell(new_coord):
                if entity is Herbivore:
                    new_entity = self._create_herbivore(new_coord)
                elif entity is Predator:
                    new_entity = self._create_predator(new_coord)
                else:
                    new_entity = entity(new_coord)
                self.game_map.set_entity(new_coord, new_entity)
                entities_createed += 1

    def _create_herbivore(self, new_coord: Coordinates):
        creature_parameters = self._get_creature_parameters()
        hp = creature_parameters["hp"]
        speed = creature_parameters["speed"]
        return choice(self.HERBIVORES)(new_coord, hp, speed)

    def _create_predator(self, new_coord: Coordinates):
        creature_parameters = self._get_creature_parameters(is_predator=True)
        hp = creature_parameters["hp"]
        speed = creature_parameters["speed"]
        attack_power = creature_parameters["attack_power"]
        return choice(self.PREDATORS)(new_coord, hp, speed, attack_power)

    def _get_creature_parameters(self, is_predator=False):
        creature_parameters = {}
        if is_predator:
            hp = randint(7, 20)
            speed = randint(1, 3)
            attack_power = randint(1, 3)
            creature_parameters["attack_power"] = attack_power
        else:
            hp = randint(10, 25)
            speed = randint(1, 2)
        creature_parameters["hp"] = hp
        creature_parameters["speed"] = speed
        return creature_parameters

    def _get_random_coordinates(self) -> Coordinates:
        new_coord_x = randint(0, self.game_map.width - 1)
        new_coord_y = randint(0, self.game_map.height - 1)
        return Coordinates(new_coord_x, new_coord_y)
