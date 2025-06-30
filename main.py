# main.py

from factory import CarWashProgramFactory
from discount import NoDiscount, ReturningCustomer


def simulate_happy_path(program_code: str, returning: bool = False) -> None:
    """
    Simulates a typical car wash interaction (happy path).

    Steps:
    1. Determine if the customer is returning.
    2. Select the appropriate wash program and discount strategy.
    3. Simulate the full wash sequence and print outputs.
    4. Show the final price after discount.

    Args:
        program_code (str): Program identifier ('A', 'B', or 'C').
        returning (bool): Whether the customer is a returning customer.
    """

    # Step 1 & 2: Determine discount strategy based on customer status
    if returning:
        print("An employee selects the program and applies a discount for a known, regular customer.")
        discount = ReturningCustomer()
    else:
        print("An employee selects the program without a discount.")
        discount = NoDiscount()

    # Step 3: Instantiate the appropriate car wash program with the discount strategy
    wash = CarWashProgramFactory.get_program(program_code, discount)

    # Step 4: Run the full wash sequence and pricing (output handled inside .run())
    wash.run()


if __name__ == "__main__":
    # === Demo Parameters ===
    PROGRAM = "B"  # Can be "A", "B", or "C"
    RETURNING = True  # Set to False to simulate a new customer

    simulate_happy_path(PROGRAM, RETURNING)
