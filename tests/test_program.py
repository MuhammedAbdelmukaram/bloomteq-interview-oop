import unittest
from unittest.mock import patch


from factory import CarWashProgramFactory
from discount import NoDiscount, ReturningCustomer, DiscountStrategy


class TestCarWashSystem(unittest.TestCase):

    def test_all_programs_with_no_discount(self):
        expected_prices = {'A': 5.0, 'B': 10.0, 'C': 15.0}
        for code, expected in expected_prices.items():
            with self.subTest(code=code):
                program = CarWashProgramFactory.get_program(code, NoDiscount())
                price = program.run()
                self.assertAlmostEqual(price, expected)

    def test_all_programs_with_10_percent_discount(self):
        expected_prices = {'A': 4.5, 'B': 9.0, 'C': 13.5}
        for code, expected in expected_prices.items():
            with self.subTest(code=code):
                program = CarWashProgramFactory.get_program(code, ReturningCustomer())
                price = program.run()
                self.assertAlmostEqual(price, expected)

    def test_program_output_steps_basic(self):
        with patch("builtins.print") as mocked_print:
            program = CarWashProgramFactory.get_program("A")
            program.run()

        calls = [call.args[0] for call in mocked_print.call_args_list]
        self.assertIn("Washing with water", calls)
        self.assertIn("Drying car", calls)
        self.assertNotIn("Applying soap", calls)
        self.assertNotIn("Polishing car", calls)

    def test_program_output_steps_deluxe(self):
        with patch("builtins.print") as mocked_print:
            program = CarWashProgramFactory.get_program("C")
            program.run()

        calls = [call.args[0] for call in mocked_print.call_args_list]
        self.assertIn("Washing with water", calls)
        self.assertIn("Applying soap", calls)
        self.assertIn("Drying car", calls)
        self.assertIn("Polishing car", calls)

    def test_discount_precision(self):
        class PreciseDiscount(DiscountStrategy):
            def apply(self, price):
                return price * 0.875  # 12.5% off

        program = CarWashProgramFactory.get_program("C", PreciseDiscount())
        price = program.run()
        self.assertAlmostEqual(price, 13.125)

    def test_case_insensitive_program_codes(self):
        for code in ['a', 'b', 'c', 'A', 'B', 'C']:
            with self.subTest(code=code):
                program = CarWashProgramFactory.get_program(code)
                self.assertIsNotNone(program)

    def test_missing_discount_defaults_to_no_discount(self):
        program = CarWashProgramFactory.get_program("A")
        self.assertAlmostEqual(program.run(), 5.0)

    def test_invalid_program_raises(self):
        for bad in ["X", "", " ", None, 123]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    CarWashProgramFactory.get_program(bad)

    def test_discount_more_than_100_percent(self):
        class TooMuchDiscount(DiscountStrategy):
            def apply(self, price):
                return price * -0.1

        program = CarWashProgramFactory.get_program("A", TooMuchDiscount())
        price = program.run()
        self.assertLess(price, 0.0)

    def test_zero_price_program(self):
        class FreeWashProgram(CarWashProgramFactory._mapping["A"]):
            def calculate_price(self):
                return 0.0

        program = FreeWashProgram(NoDiscount())
        self.assertEqual(program.run(), 0.0)

    def test_incomplete_program_raises(self):
        from program import CarWashProgram

        class BrokenProgram(CarWashProgram):
            def requires_soap(self): return True
            def requires_polish(self): return False
            # forgot calculate_price()

        with self.assertRaises(TypeError):
            BrokenProgram(NoDiscount())  # abstract method not implemented

    def test_tiered_discount_logic(self):
        class TieredDiscount(DiscountStrategy):
            def apply(self, price):
                if price > 10:
                    return price * 0.80  # 20% off
                return price * 0.90  # 10% off

        deluxe = CarWashProgramFactory.get_program("C", TieredDiscount())  # $15 → 20% off → $12
        basic = CarWashProgramFactory.get_program("A", TieredDiscount())  # $5  → 10% off → $4.5

        self.assertAlmostEqual(deluxe.run(), 12.0)
        self.assertAlmostEqual(basic.run(), 4.5)

    def test_run_returns_float(self):
        program = CarWashProgramFactory.get_program("B", ReturningCustomer())
        result = program.run()
        self.assertIsInstance(result, float)


if __name__ == "__main__":
    unittest.main()
