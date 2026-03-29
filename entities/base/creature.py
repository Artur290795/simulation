from __future__ import annotations
from abc import abstractmethod
from collections import deque

from entities.base.entity import Entity
from core.coordinates import Coordinates


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, hp: int, speed: int):
        super().__init__(coordinates)
        self.hp = hp
        self.speed = speed

    @abstractmethod
    def make_move(self, game_map: "Map"):  # строковая аннотация
        pass

    def next_cell_to_target(
        self, game_map: "Map", start_cell: Coordinates, is_target_cell
    ) -> Coordinates:
        queue = deque()
        queue.append(start_cell)
        visited_cells = set()
        visited_cells.add(start_cell)
        parent = {}
        while queue:
            current_cell = queue.popleft()
            if is_target_cell(current_cell):
                path = []
                while current_cell != start_cell:
                    path.append(current_cell)
                    current_cell = parent[current_cell]
                path.reverse()
                return path[0]
            neighbour_cells_offsets = ((-1, 0), (1, 0), (0, -1), (0, 1)) # я здесь криво реализовал
            for x_offset, y_offset in neighbour_cells_offsets:                                               # если скорость 3, то надо что бы
                new_x, new_y = current_cell.x + x_offset, current_cell.y + y_offset                          # соседями были все ячейки от 1 до 3
                neighbour_cell = Coordinates(new_x, new_y)                                                   # ну кароче сильно больше их будет
                if not game_map.is_valid_coordinates(neighbour_cell):
                    continue
                if neighbour_cell not in visited_cells and game_map.is_walkable_cell(
                    neighbour_cell, self
                ):
                    visited_cells.add(neighbour_cell)
                    parent[neighbour_cell] = current_cell
                    queue.append(neighbour_cell)
        return None
