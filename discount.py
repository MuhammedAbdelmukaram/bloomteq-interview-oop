from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        ...


class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price


class ReturningCustomer(DiscountStrategy):

    def __init__(self, percent: float = 10.0):
        self.percent = percent

    def apply(self, price: float) -> float:
        return price * (1 - self.percent / 100)
