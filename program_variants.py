from program import CarWashProgram


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
