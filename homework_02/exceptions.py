"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self, message="LowFuelError"):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    def __init__(self, message="NotEnoughFuel"):
        self.message = message
        super().__init__(self.message)

class CargoOverload(Exception):
    def __init__(self, message="CargoOverload"):
        self.message = message
        super().__init__(self.message)