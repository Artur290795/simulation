from entities.entity import Entity
from entities.grass import Grass
from entities.rock import Rock
from entities.tree import Tree
from entities.herbivores.antelope import Antelope
from entities.herbivores.giraffe import Giraffe
from entities.herbivores.zebra import Zebra
from entities.predators.lion import Lion
from entities.predators.hyena import Hyena
from entities.predators.leopard import Leopard
from entities.herbivores.herbivore import Herbivore
from entities.predators.predator import Predator
from entities.creature import Creature  # для аннотации is_walkable_cell
from enums.coordinates import Coordinates


class Map:
    def __init__(self, width, height):
        self.game_map = {}
        self.width = width
        self.height = height

    def setup_default_positions(self):
        self.set_entity(Coordinates(1, 1), Lion(Coordinates(1, 1), 10, 1, 2))
        self.set_entity(Coordinates(2, 2), Leopard(Coordinates(2, 2), 8, 11, 2))
        self.set_entity(Coordinates(3, 3), Hyena(Coordinates(3, 3), 6, 4, 1))
        self.set_entity(Coordinates(4, 4), Giraffe(Coordinates(4, 4), 10, 2))
        self.set_entity(Coordinates(5, 5), Zebra(Coordinates(5, 5), 8, 4))
        self.set_entity(Coordinates(6, 6), Antelope(Coordinates(6, 6), 5, 5))
        self.set_entity(Coordinates(7, 7), Grass(Coordinates(7, 7)))
        self.set_entity(Coordinates(8, 8), Rock(Coordinates(8, 8)))
        self.set_entity(Coordinates(9, 9), Tree(Coordinates(9, 9)))

    def set_entity(self, coordinates: Coordinates, entity: Entity):
        if self.is_valid_coordinates(coordinates):
            entity.coordinates = coordinates
            self.game_map[coordinates] = entity
            return
        raise ValueError(f"Координаты {coordinates} вне границ карты")

    def get_entity(self, coordinates: Coordinates):
        entity = self.game_map.get(coordinates, None)
        return entity

    def remove_entity(self, coordinates: Coordinates):
        if coordinates in self.game_map:
            del self.game_map[coordinates]

    def is_valid_coordinates(self, coordinates: Coordinates):
        return 0 <= coordinates.x < self.width and 0 <= coordinates.y < self.height

    def clear(self):
        self.game_map.clear()

    def move(self):
        for coordinates, entity in self.game_map.items():
            self.game_map[coordinates] = ""
            self.game_map[Coordinates(coordinates.x + 1, coordinates.y)] = entity

    def is_walkable_cell(self, coordinates: Coordinates, creature: Creature) -> bool:
        cell_value = self.game_map.get(coordinates, None)
        if cell_value is None:
            return True
        if isinstance(creature, Herbivore) and isinstance(cell_value, Grass):
            return True
        if isinstance(creature, Predator) and isinstance(cell_value, Grass):
            return True
        return False

    def is_empty_cell(self, coordinates: Coordinates):
        return self.game_map.get(coordinates, None) is None
