from abc import ABC, abstractmethod


class CarWashProgram(ABC):
    """
    Abstract base class representing a car wash program.
    Implements the Template Method pattern: defines the wash sequence
    and delegates variable parts (like soap, polish, price) to subclasses.
    """

    def __init__(self, discount_strategy):
        """
        Initialize with a discount strategy.

        Args:
            discount_strategy: An object implementing the DiscountStrategy interface.
        """
        self.discount_strategy = discount_strategy

    def run(self):
        """
        Execute the full car wash program:
        - Print entry message
        - Run wash sequence
        - Apply discount to base price
        - Print total and exit message

        Returns:
            float: Final price after applying discount.
        """
        print("Car entering car wash")
        self._wash_sequence()
        print("Car exiting car wash")

        base = self.calculate_price()
        total = self.discount_strategy.apply(base)

        print("Total:", total)
        return total

    def _wash_sequence(self):
        """
        Internal method to simulate each step of the wash process.
        Steps are conditionally executed based on subclass logic.
        """
        self.water_wash()

        if self.requires_soap():
            self.apply_soap()

        self.dry()

        if self.requires_polish():
            self.polish()

    def water_wash(self):
        """Simulate water wash step."""
        print("Washing with water")

    def polish(self):
        """Simulate polish step."""
        print("Polishing car")

    def dry(self):
        """Simulate drying step."""
        print("Drying car")

    def apply_soap(self):
        """Simulate applying soap."""
        print("Applying soap")

    @abstractmethod
    def requires_soap(self) -> bool:
        """
        Determine whether soap should be used.

        Returns:
            bool: True if soap should be applied, False otherwise.
        """
        ...

    @abstractmethod
    def requires_polish(self) -> bool:
        """
        Determine whether polish should be applied.

        Returns:
            bool: True if polish should be applied, False otherwise.
        """
        ...

    @abstractmethod
    def calculate_price(self) -> float:
        """
        Calculate base price of the wash program (before discount).

        Returns:
            float: Base price.
        """
        ...


class BasicWash(CarWashProgram):
    """
    Basic car wash: only water wash and dry, no soap or polish.
    """

    def requires_soap(self) -> bool:
        return False

    def requires_polish(self) -> bool:
        return False

    def calculate_price(self) -> float:
        return 5.0


class SoapWash(CarWashProgram):
    """
    Mid-tier wash: includes soap but no polish.
    """

    def requires_soap(self) -> bool:
        return True

    def requires_polish(self) -> bool:
        return False

    def calculate_price(self) -> float:
        return 10.0


class DeluxeWash(CarWashProgram):
    """
    Premium wash: includes both soap and polish.
    """

    def requires_soap(self) -> bool:
        return True

    def requires_polish(self) -> bool:
        return True

    def calculate_price(self) -> float:
        return 15.0
