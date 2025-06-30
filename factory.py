from discount import DiscountStrategy, NoDiscount
from program import BasicWash, SoapWash, DeluxeWash, CarWashProgram


class CarWashProgramFactory:
    _mapping = {
        "A": BasicWash,
        "B": SoapWash,
        "C": DeluxeWash
    }

    @staticmethod
    def get_program(code: str, discount: DiscountStrategy = None) -> CarWashProgram:

        if not isinstance(code, str):
            raise ValueError("Program Received Wrong Letter")

        cls = CarWashProgramFactory._mapping.get(code.upper())

        if cls is None:
            raise ValueError("Wrong Letter Sent")

        return cls(discount or NoDiscount())
