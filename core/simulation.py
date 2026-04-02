"""
Модуль для класса симуляции
"""

from PySide6.QtWidgets import QGraphicsView, QMessageBox
from PySide6.QtCore import QObject, QTimer, Signal

from entities.base.creature import Creature
from entities.static.grass import Grass
from entities.herbivores.herbivore import Herbivore
from entities.predators.predator import Predator
from core.game_map import Map
from core.renderer import MapRenderer


class Simulation(QObject):
    """
    Главный класс приложения, включает в себя:
        - Карту
        - Счётчик ходов
        - Рендерер поля
        - next_turn() - просимулировать и отрендерить один ход
        - start_simulation() - запустить бесконечный цикл симуляции и рендеринга
        - pause_simulation() - приостановить бесконечный цикл симуляции и рендеринга
        - reset_simulation() - перезапустить симуляцию
    """

    data_changed = Signal()

    def __init__(
        self, predators_amount: int, herbivores_amount: int, width=20, height=20
    ):
        super().__init__()
        self.game_map = Map(width, height, predators_amount, herbivores_amount)
        self.width = width
        self.height = height
        self.map_renderer = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_turn)
        self.is_running = False
        self.game_counter = 0
        self.map_view = None
        self.predators_amount = None
        self.herbivores_amount = None
        self.grasses_amount = None
        self.game_map.setup_default_positions()

    def start_simulation(self):
        if not self.is_running:
            self.is_running = True
            delay = 1200
            self.timer.start(delay)
            self.update_world_info()

    def next_turn(self):
        creatures = [
            x for x in self.game_map.game_map.values() if isinstance(x, Creature)
        ]
        for creature in creatures:
            if creature.coordinates is not None:
                creature.make_move(self.game_map)
                if creature.hp <= 0:
                    self.game_map.remove_entity(creature.coordinates)

        new_grass_amount = 1
        self.game_map.entity_factory.create_entities(new_grass_amount, Grass)
        self.map_renderer.render(self.game_map)

        if len(creatures) == 0:
            self.pause_simulation()
            QMessageBox.information(
                None, "Завершение симуляции", "Все существа вымерли, симуляция окончена"
            )
        self.update_world_info()

    def pause_simulation(self):
        self.timer.stop()
        self.is_running = False

    def reset_simulation(self):
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
        self.data_changed.emit()
