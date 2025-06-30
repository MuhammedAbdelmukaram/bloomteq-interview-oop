from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """
    Abstract base class representing a discount strategy.
    Subclasses must implement the `apply` method to modify the given price.
    """

    @abstractmethod
    def apply(self, price: float) -> float:
        """
        Apply a discount to the given price.

        Args:
            price (float): The original price before discount.

        Returns:
            float: The price after applying the discount.
        """
        ...


class NoDiscount(DiscountStrategy):
    """
    Concrete discount strategy that applies no discount.
    """

    def apply(self, price: float) -> float:
        """
        Return the price unchanged.

        Args:
            price (float): The original price.

        Returns:
            float: Same as the input price.
        """
        return price


class ReturningCustomer(DiscountStrategy):
    """
    Concrete discount strategy for returning customers.
    Applies a fixed percentage discount to the original price.
    """

    def __init__(self, percent: float = 10.0):
        """
        Initialize with a discount percentage.

        Args:
            percent (float): Discount percentage to apply (default is 10%).
        """
        self.percent = percent

    def apply(self, price: float) -> float:
        """
        Apply the discount percentage to the original price.

        Args:
            price (float): The original price.

        Returns:
            float: Price after applying the percentage discount.
        """
        return price * (1 - self.percent / 100)
