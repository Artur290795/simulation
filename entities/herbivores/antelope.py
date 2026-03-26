from entities.herbivores.herbivore import Herbivore


class Antelope(Herbivore):
    def __init__(self, coordinates, hp, speed):
        super().__init__(coordinates, hp, speed)