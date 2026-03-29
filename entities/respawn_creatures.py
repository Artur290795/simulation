from __future__ import annotations
from random import randint, choice

from entities.static.grass import Grass
from entities.herbivores.antelope import Antelope
from entities.herbivores.giraffe import Giraffe
from entities.herbivores.herbivore import Herbivore
from entities.herbivores.zebra import Zebra
from entities.predators.hyena import Hyena
from entities.predators.leopard import Leopard
from entities.predators.lion import Lion
from entities.predators.predator import Predator
from entities.static.rock import Rock
from entities.static.tree import Tree
from core.coordinates import Coordinates


class CreatureSpawner:
    PREDATORS = [Lion, Leopard, Hyena]
    HERBIVORES = [Antelope, Giraffe, Zebra]

    def __init__(self, game_map: "Map", predators_amount: int, herbivores_amount: int):
        self.game_map = game_map
        self.predators_amount = predators_amount
        self.herbivores_amount = herbivores_amount
        self.grasses_amount = int(herbivores_amount * 2.5)
        self.rocks_amount = (predators_amount + herbivores_amount) // 2
        self.trees_amount = (predators_amount + herbivores_amount) // 2

    def respawn(self):
        self.respawn_creatures(self.predators_amount, Predator)
        self.respawn_creatures(self.herbivores_amount, Herbivore)
        self.respawn_creatures(self.grasses_amount, Grass)
        self.respawn_creatures(self.rocks_amount, Rock)
        self.respawn_creatures(self.trees_amount, Tree)

    def respawn_creatures(self, creature_amount: int, entity: type):
        creature_respawned = 0
        while creature_respawned < creature_amount:
            new_coord = self._get_random_coordinates()
            if self.game_map.is_empty_cell(new_coord):
                if entity is Herbivore:
                    new_entity = self._respawn_herbivore(new_coord)
                elif entity is Predator:
                    new_entity = self._respawn_predator(new_coord)
                else:
                    new_entity = entity(new_coord)
                self.game_map.set_entity(new_coord, new_entity)
                creature_respawned += 1

    def _respawn_herbivore(self, new_coord: Coordinates):
        creature_parameters = self._get_creature_parameters()
        hp = creature_parameters["hp"]
        speed = creature_parameters["speed"]
        return choice(self.HERBIVORES)(new_coord, hp, speed)

    def _respawn_predator(self, new_coord: Coordinates):
        creature_parameters = self._get_creature_parameters(is_predator=True)
        hp = creature_parameters["hp"]
        speed = creature_parameters["speed"]
        attack_power = creature_parameters["attack_power"]
        return choice(self.PREDATORS)(new_coord, hp, speed, attack_power)

    def _get_creature_parameters(self, is_predator=False):
        creature_parameters = {}
        if is_predator:
            hp = randint(7, 20)
            speed = randint(2, 5)
            attack_power = randint(2, 4)
            creature_parameters["attack_power"] = attack_power
        else:
            hp = randint(10, 25)
            speed = randint(4, 9)
        creature_parameters["hp"] = hp
        creature_parameters["speed"] = speed
        return creature_parameters

    def _get_random_coordinates(self) -> Coordinates:
        new_coord_x = randint(0, self.game_map.width - 1)
        new_coord_y = randint(0, self.game_map.height - 1)
        return Coordinates(new_coord_x, new_coord_y)
