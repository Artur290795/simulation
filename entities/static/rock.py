from entities.base.entity import Entity
from core.coordinates import Coordinates


class Rock(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)