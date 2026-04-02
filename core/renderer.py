"""
Отрисовывает карту в графическом интерфейсе с использованием PySide6
"""

from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QFont


from entities.base.entity import Entity
from core.coordinates import Coordinates
from core.game_map import Map

from entities.static.grass import Grass
from entities.herbivores.antelope import Antelope
from entities.herbivores.giraffe import Giraffe
from entities.herbivores.zebra import Zebra
from entities.herbivores.herbivore import Herbivore
from entities.predators.predator import Predator
from entities.predators.hyena import Hyena
from entities.predators.leopard import Leopard
from entities.predators.lion import Lion
from entities.static.rock import Rock
from entities.static.tree import Tree


class MapRenderer(QGraphicsView):
    """
    Визуализирует карту как сетку клеток с эмодзи и всплывающими подсказками
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.cell_size = 35
        self.game_map = None

    def render(self, game_map: Map):
        self._scene.clear()
        self.game_map = game_map
        width = game_map.width * self.cell_size
        height = game_map.height * self.cell_size
        self._scene.setSceneRect(0, 0, width, height)

        for y in range(game_map.height):
            for x in range(game_map.width):
                self._draw_cell(x, y)

    def _draw_cell(self, x: int, y: int) -> None:
        entity = self.game_map.get_entity(Coordinates(x, y))
        rect = QGraphicsRectItem(
            x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size
        )

        color = QColor(255, 235, 190)
        tooltip = self._get_tooltip(entity)
        if tooltip:
            rect.setToolTip(tooltip)
        rect.setBrush(QBrush(color))
        rect.setPen(QPen(Qt.black))
        self._scene.addItem(rect)

        emoji = self._get_emoji(entity)
        if emoji:
            text = QGraphicsTextItem(emoji)
            if tooltip:
                text.setToolTip(tooltip)
            font = QFont("Segoe UI Emoji", self.cell_size // 2)
            text.setFont(font)
            text.setDefaultTextColor(Qt.black)
            text.setPos(
                x * self.cell_size + (self.cell_size - text.boundingRect().width()) / 2,
                y * self.cell_size
                + (self.cell_size - text.boundingRect().height()) / 2,
            )
            self._scene.addItem(text)

    def update_cell(self, x: int, y: int) -> None:
        items = self._scene.items(
            x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size
        )
        for item in items:
            self._scene.removeItem(item)
        self._draw_cell(x, y)

    def _get_tooltip(self, entity: Entity | None):
        if entity is None:
            return ""
        if isinstance(entity, Grass):
            return "🌿 Трава"
        if isinstance(entity, Rock):
            return "🪨 Камень"
        if isinstance(entity, Tree):
            return "🌳 Дерево"
        if isinstance(entity, Herbivore):
            return f"🦒 Травоядное\n❤️ HP: {entity.hp}\n⚡ Скорость: {entity.speed}"
        if isinstance(entity, Predator):
            return f"🦁 Хищник\n❤️ HP: {entity.hp}\n⚡ Скорость: {entity.speed}\n⚔️ Атака: {entity.attack_power}"
        return str(type(entity).__name__)

    @staticmethod
    def _get_emoji(entity: Entity) -> None:
        if isinstance(entity, Leopard):
            return "🐆"  # или "🦌"
        elif isinstance(entity, Lion):
            return "🦁"
        elif isinstance(entity, Hyena):
            return "🐺"
        elif isinstance(entity, Giraffe):
            return "🦒"
        elif isinstance(entity, Antelope):
            return "🦌"
        elif isinstance(entity, Zebra):
            return "🦓"
        elif isinstance(entity, Grass):
            return "🌿"
        elif isinstance(entity, Tree):
            return "🌳"
        elif isinstance(entity, Rock):
            return "⛰️"
        return ""
