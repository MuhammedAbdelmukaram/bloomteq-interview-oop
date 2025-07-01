#  Bloomteq OOP Task - Car Wash Simulation

This project simulates a modular and extensible car wash facility that supports multiple wash programs and customer discounts. It is implemented using object-oriented design principles, clean architecture, and a fully tested strategy-driven pricing model.

---

##  Table of Contents

1. [Problem Description](#-problem-description)
2. [Design Principles & Decisions](#-design-principles-&-decisions)  
3. [Design Patterns Used](#-design-patterns-used)  
4. [Getting Started](#-getting-started)  
5. [Testing](#-testing)  
6. [Contact](#contact)

---

##  Problem Description

Simulate a car wash facility that supports several predefined wash programs. Each program includes a combination of steps like water wash, soap, drying, and polishing. Customers may optionally receive a discount if they are returning clients.

**Example Programs:**

- **Program A**: Water wash + Dry
- **Program B**: Water wash + Soap + Dry
- **Program C**: Water wash + Soap + Dry + Polish

At runtime:
- The employee selects a program.
- If the customer is returning, a discount is applied.
- Steps are simulated via console output.
- Final price is calculated and printed after discount.

---

##  Design Principles & Decisions

This simulation was implemented with maintainability, extensibility, and testability in mind:

- **Object-Oriented Design**: The system is broken into logical abstractions (`CarWashProgram`, `Discount`) with clear responsibilities.
- **Open/Closed Principle**: New wash programs or discount types can be added without modifying existing logic.
- **Separation of Concerns**: Discount logic and wash sequence logic are decoupled.
- **Composition over Inheritance**: Discount strategies are passed into wash programs via constructor injection, enabling flexible combinations.
- **Polymorphism**: Used to allow different behavior across program variants (A/B/C) through common interfaces.
- **Template Method Pattern**: Allows all wash programs to share the same high-level flow while customizing steps like `apply_soap()` and pricing.

These choices result in a modular and testable architecture that supports future extensions with minimal changes.


## 💡 Design Patterns Used

| Pattern             | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| **Strategy**         | Flexible discount logic (`DiscountStrategy`, `NoDiscount`, `ReturningCustomer`) |
| **Template Method**  | Defines the common wash flow, with overridable steps (`CarWashProgram`) |
| **Factory**          | Maps user input to concrete program classes (`CarWashProgramFactory`)   |
| **Composition**      | Injects discount logic into wash programs via constructor              |

---

##  Getting Started

### Prerequisites

- Python 3.7 or newer


Run the simulation from main.py:


python main.py
You can change the simulation scenario in main.py:


PROGRAM = "B"       # Choose from "A", "B", "C"
RETURNING = True    # Set to True for discount



##  Testing

The project uses `unittest` with comprehensive coverage for:

- All car wash programs (A, B, C) with and without discounts
- Custom discount scenarios (e.g., >100%, tiered, 0%)
- Edge cases like missing methods, invalid inputs, and zero-price programs
- Case-insensitive code parsing (`'a' == 'A'`)

To run tests:

```bash
python -m unittest tests/test_program.py
```

---

## Contact

Muhammed Abdelmukaram - [m.abdelmukaram@outlook.com](mailto:m.abdelmukaram@outlook.com) 
GitHub: https://github.com/MuhammedAbdelmukaram/bloomteq-interview-tasks
