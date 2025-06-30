#main.py

from factory import CarWashProgramFactory
from discount import NoDiscount, ReturningCustomer


def simulate_happy_path(program_code: str, returning: bool = False) -> None:

    # 2. An employee selects the program (and discount if returning).
    if returning:
        print("An employee selects the program and applies a discount for a known, regular customer.")
        discount = ReturningCustomer()
    else:
        print("An employee selects the program without a discount.")
        discount = NoDiscount()

    # instantiate & run the wash
    wash = CarWashProgramFactory.get_program(program_code, discount)

    # 3 & 4: steps + final price are printed inside .run()
    wash.run()


if __name__ == "__main__":
    # *** demo parameters ***
    PROGRAM = "B"  # Change to A, B or C
    RETURNING = True  # Change to False to skip discount

    simulate_happy_path(PROGRAM, RETURNING)
