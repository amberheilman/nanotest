import unittest
import main


class ValidateQuantityTest(unittest.TestCase):

    def should_return_true_on_valid_input(self):
        returned = main.validate_quantity(5)
        self.assertTrue(returned)


if __name__ == '__main__':
    unittest.main()
