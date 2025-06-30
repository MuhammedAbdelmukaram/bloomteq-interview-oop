from discount import DiscountStrategy, NoDiscount
from program import  CarWashProgram
from program_variants import BasicWash, SoapWash, DeluxeWash


class CarWashProgramFactory:
    """
    Factory class to create car wash program instances based on a given code.
    Uses a simple lookup dictionary to map program codes ('A', 'B', 'C') to corresponding classes.
    """

    _mapping = {
        "A": BasicWash,    # Program A → Basic (water + dry)
        "B": SoapWash,     # Program B → Adds soap
        "C": DeluxeWash    # Program C → Adds soap and polish
    }

    @staticmethod
    def get_program(code: str, discount: DiscountStrategy = None) -> CarWashProgram:
        """
        Static method to retrieve a car wash program based on the code.

        Args:
            code (str): A single character string representing the program code ('A', 'B', or 'C').
            discount (DiscountStrategy, optional): A discount strategy instance. Defaults to NoDiscount.

        Returns:
            CarWashProgram: An instance of the corresponding car wash program.

        Raises:
            ValueError: If the code is not a string or does not match a known program.
        """
        if not isinstance(code, str):
            raise ValueError("Program Received Wrong Letter")  # Defensive check: only accept strings

        cls = CarWashProgramFactory._mapping.get(code.upper())  # Case-insensitive lookup

        if cls is None:
            raise ValueError("Wrong Letter Sent")  # Handle unknown program code

        # Instantiate the program with the given discount strategy (or NoDiscount by default)
        return cls(discount or NoDiscount())
