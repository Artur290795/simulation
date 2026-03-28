from time import sleep
from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import QTimer
from entities.base.creature import Creature
from entities.static.grass import Grass
from entities.herbivores.herbivore import Herbivore
from entities.predators.predator import Predator
from core.game_map import Map
from core.renderer import MapRenderer


class Simulation:
    def __init__(
        self, predators_amount: int, herbivores_amount: int, width=20, height=20
    ):
        self.game_map = Map(width, height, predators_amount, herbivores_amount)
        self.width = width
        self.height = height
        self.map_renderer = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.turn_actions)
        self.is_running = False
        print(f"Создана карта размером {width} на {height}")
        self.game_counter = 0
        self.map_view = None
        self.predators_amount = None
        self.herbivores_amount = None
        self.grasses_amount = None
        self.game_map.setup_default_positions()

    def start_actions(self):
        if not self.is_running:
            self.is_running = True
            # delay = self.map_view.speedSlider.value() if self.map_view else 200
            delay = 1500
            self.timer.start(delay)
            self.update_world_info()

    def turn_actions(self):
        if not self.is_running:
            return
        creatures = [
            x for x in self.game_map.game_map.values() if isinstance(x, Creature)
        ]
        for creature in creatures:
            if creature.coordinates is not None:
                creature.make_move(self.game_map)
        self.map_renderer.render(self.game_map)
        self.update_world_info()

        if self.herbivores_amount == 0:
            self.pause_actions()

    def pause_actions(self):
        self.timer.stop()
        self.is_running = False

    def reset_actions(self):
        self.timer.stop()
        self.is_running = False
        self.game_map.clear()
        self.game_map.setup_default_positions()
        self.game_counter = 0
        self.map_renderer.render(self.game_map)
        self.update_world_info()

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
        self.map_renderer.render(self.game_map)

    def update_world_info(self):
        self.game_counter += 1
        self.predators_amount = len(
            [x for x in self.game_map.game_map.values() if isinstance(x, Predator)]
        )
        self.herbivores_amount = len(
            [x for x in self.game_map.game_map.values() if isinstance(x, Herbivore)]
        )
        self.grasses_amount = len(
            [x for x in self.game_map.game_map.values() if isinstance(x, Grass)]
        )
