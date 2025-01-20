from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel <= 0:
            raise LowFuelError
        elif not self.started:
            self.started = True

    def move(self, distance):
        fuel_for_distance = distance*self.fuel_consumption
        if self.fuel-fuel_for_distance >= 0:
            self.fuel -= fuel_for_distance
        else:
            raise NotEnoughFuel
