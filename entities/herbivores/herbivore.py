from __future__ import annotations
from entities.creature import Creature
from entities.grass import Grass
from enums.coordinates import Coordinates


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, hp: int, speed: int):
        super().__init__(coordinates, hp, speed)

    def make_move(self, game_map: "Map"):
        next_cell = self.find_path_to_target(
            game_map,
            self.coordinates,
            is_target_cell=lambda cell: isinstance(
                game_map.get_entity(Coordinates(cell.x, cell.y)), Grass
            ),
        )
        if next_cell is None:
            return
        target_entity = game_map.get_entity(Coordinates(next_cell.x, next_cell.y))
        if isinstance(target_entity, Grass):
            game_map.remove_entity(Coordinates(next_cell.x, next_cell.y))
            game_map.remove_entity(self.coordinates)
            game_map.set_entity(Coordinates(next_cell.x, next_cell.y), self)

        else:
            game_map.remove_entity(Coordinates(self.coordinates.x, self.coordinates.y))
            self.coordinates = next_cell
            game_map.set_entity(next_cell, self)
