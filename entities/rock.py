from entities.entity import Entity
from enums.coordinates import Coordinates


class Rock(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)