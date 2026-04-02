"""
    Реализует игровое поле
"""
from entities.base.entity import Entity
from entities.entity_factory import EntityFactory
from entities.static.grass import Grass
from entities.herbivores.herbivore import Herbivore
from entities.predators.predator import Predator
from entities.base.creature import Creature
from core.coordinates import Coordinates



class Map:
    """
    Хранит сущности в словаре game_map с ключами Coordinates
    """
    def __init__(self, width, height, predators_amount: int, herbivores_amount: int):
        self.game_map = {}
        self.width = width
        self.height = height
        self.entity_factory = EntityFactory(self, predators_amount, herbivores_amount)

    def setup_default_positions(self):
        self.entity_factory.create()

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
            entity = self.game_map[coordinates]
            entity.coordinates = None
            del self.game_map[coordinates]

    def is_valid_coordinates(self, coordinates: Coordinates):
        return 0 <= coordinates.x < self.width and 0 <= coordinates.y < self.height

    def clear(self):
        self.game_map.clear()

    def move(self):
        pass

    def is_walkable_cell(self, coordinates: Coordinates, creature: Creature) -> bool:
        cell_value = self.game_map.get(coordinates, None)
        if cell_value is None:
            return True
        if isinstance(creature, Herbivore) and isinstance(cell_value, Grass):
            return True
        if isinstance(creature, Predator) and isinstance(cell_value, Herbivore):
            return True
        return False

    def is_empty_cell(self, coordinates: Coordinates):
        return self.game_map.get(coordinates, None) is None
