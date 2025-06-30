from abc import ABC, abstractmethod


class CarWashProgram(ABC):
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def run(self):
        print("Car entering car wash")
        self._wash_sequence()
        print("Car exiting car wash")

        base = self.calculate_price()
        total = self.discount_strategy.apply(base)

        print("Total:", total)

        return total

    def _wash_sequence(self):
        self.water_wash()

        if self.requires_soap():
            self.apply_soap()

        self.dry()

        if self.requires_polish():
            self.polish()

    def water_wash(self):
        print("Washing with water")

    def polish(self):
        print("Polishing car")

    def dry(self):
        print("Drying car")

    def apply_soap(self):
        print("Applying soap")

    @abstractmethod
    def requires_soap(self) -> bool:
        ...

    @abstractmethod
    def requires_polish(self) -> bool:
        ...

    @abstractmethod
    def calculate_price(self) -> float:
        ...


class BasicWash(CarWashProgram):
    def requires_soap(self) -> bool:
        return False

    def requires_polish(self) -> bool:
        return False

    def calculate_price(self) -> float:
        return 5.0


class SoapWash(CarWashProgram):
    def requires_soap(self) -> bool:
        return True

    def requires_polish(self) -> bool:
        return False

    def calculate_price(self) -> float:
        return 10.0


class DeluxeWash(CarWashProgram):
    def requires_soap(self) -> bool:
        return True

    def requires_polish(self) -> bool:
        return True

    def calculate_price(self) -> float:
        return 15.0
