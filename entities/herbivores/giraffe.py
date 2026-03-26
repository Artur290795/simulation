from entities.herbivores.herbivore import Herbivore


class Giraffe(Herbivore):
    def __init__(self, coordinates, hp, speed):
        super().__init__(coordinates, hp, speed)