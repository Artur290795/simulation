from entities.entity import Entity
from enums.coordinates import Coordinates


class Grass(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
