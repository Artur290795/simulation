"""
Модуль для главного абстрактного класса всех живых существ
"""

from __future__ import annotations
from abc import abstractmethod
from collections import deque
from typing import Callable

from entities.base.entity import Entity
from core.coordinates import Coordinates


class Creature(Entity):
    """
    Класс Creature (наследник Entity)

    hp – здоровье.

    speed – количество клеток, которое может пройти за ход.

    Абстрактные методы:

    get_target_class() – возвращает класс цели (трава/травоядное).

    is_attack(target) – определяет, нужно ли атаковать цель.

    interact_with_target(target) – выполняет взаимодействие (атака/поедание).

    make_move(game_map) – общая логика хода: поиск пути до цели, учёт скорости, перемещение, голод.

    get_path_to_target(game_map, start_cell, is_target_cell) – метод для поиска кратчайшего пути и возврата всего списка клеток.
    """

    def __init__(self, coordinates: Coordinates, hp: int, speed: int):
        super().__init__(coordinates)
        self.hp = hp
        self.speed = speed

    @abstractmethod
    def get_target_class(self):
        pass

    @abstractmethod
    def is_attack(self, target):
        pass

    @abstractmethod
    def interact_with_target(self, target):
        pass

    def make_move(self, game_map: "Map"):
        path = self.get_path_to_target(
            game_map,
            self.coordinates,
            is_target_cell=lambda cell: isinstance(
                game_map.get_entity(cell), self.get_target_class()
            ),
        )
        if path is None:
            self.hp -= 1
            return
        steps = min(self.speed, len(path))
        next_cell = path[steps - 1]
        target_entity = game_map.get_entity(next_cell)
        if self.is_attack(target_entity):
            self.interact_with_target(target_entity)
            if hasattr(target_entity, "hp"):
                if target_entity.hp <= 0:
                    game_map.remove_entity(next_cell)
                    game_map.remove_entity(self.coordinates)
                    self.coordinates = next_cell
                    game_map.set_entity(next_cell, self)
            else:
                game_map.remove_entity(next_cell)
                game_map.remove_entity(self.coordinates)
                self.coordinates = next_cell
                game_map.set_entity(next_cell, self)
        else:
            game_map.remove_entity(Coordinates(self.coordinates.x, self.coordinates.y))
            self.coordinates = next_cell
            game_map.set_entity(next_cell, self)
        self.hp -= 1

    def get_path_to_target(
        self,
        game_map: "Map",
        start_cell: Coordinates,
        is_target_cell: Callable,
    ) -> Coordinates:
        queue = deque([start_cell])
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
                return path
            neighbour_cells_offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for x_offset, y_offset in neighbour_cells_offsets:
                new_x, new_y = current_cell.x + x_offset, current_cell.y + y_offset
                neighbour_cell = Coordinates(new_x, new_y)
                if not game_map.is_valid_coordinates(neighbour_cell):
                    continue
                if neighbour_cell not in visited_cells and game_map.is_walkable_cell(
                    neighbour_cell, self
                ):
                    visited_cells.add(neighbour_cell)
                    parent[neighbour_cell] = current_cell
                    queue.append(neighbour_cell)
        return None
