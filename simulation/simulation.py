from PySide6.QtWidgets import QGraphicsView
from entities.creature import Creature
from map.game_map import Map
from renderer import MapRenderer


class Simulation:
    def __init__(self, width: int, height: int):
        self.game_map = Map(width, height)
        self.width = width
        self.height = height
        print(f"Создана карта размером {width} на {height}")
        self.game_counter = 0
        self.map_renderer = None
        self.map_view = None

    def start_actions(self):
        self.game_map.clear()
        self.game_map.setup_default_positions()
        if self.map_renderer:
            self.map_renderer.render(self.game_map)

    def turn_actions(self):
        creatures = [
            x for x in self.game_map.game_map.values() if isinstance(x, Creature)
        ]
        for creature in creatures:
            if creature.coordinates is not None:
                creature.make_move(self.game_map)
        self.game_counter += 1
        if self.map_renderer:
            self.map_renderer.render(self.game_map)

    def pause_actions(self):
        print(2)

    def reset_actions(self):
        print(4)

    def set_map_view(self, map_view: QGraphicsView) -> None:
        self.map_view = map_view
        self.map_renderer = MapRenderer()
        parent_layout = self.map_view.parent().layout()
        if parent_layout:
            index = parent_layout.indexOf(self.map_view)
            if index != -1:
                parent_layout.replaceWidget(self.map_view, self.map_renderer)
                self.map_view.deleteLater()
                self.map_view = self.map_renderer
