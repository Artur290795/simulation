from entities.base.entity import Entity
from core.coordinates import Coordinates


class Grass(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
