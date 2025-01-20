"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if weight+self.cargo <= self.max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        result, self.cargo = self.cargo, 0
        return result
