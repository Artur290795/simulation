from abc import ABC, abstractmethod

from enums.coordinates import Coordinates


class Entity(ABC):
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates
