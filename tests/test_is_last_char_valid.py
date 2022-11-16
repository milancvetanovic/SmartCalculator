import unittest
from check_validity import is_last_char_valid


class TestIsLastCharValid(unittest.TestCase):
    def test_plus_operator(self):
        result = is_last_char_valid('+')
        self.assertFalse(result, "Should be False")

    def test_minus_operator(self):
        result = is_last_char_valid('-')
        self.assertFalse(result, "Should be False")

    def test_multiplication_operator(self):
        result = is_last_char_valid('*')
        self.assertFalse(result, "Should be False")

    def test_dividing_operator(self):
        result = is_last_char_valid('/')
        self.assertFalse(result, "Should be False")

    def test_open_bracket(self):
        result = is_last_char_valid('(')
        self.assertFalse(result, "Should be False")

    def test_power_operator(self):
        result = is_last_char_valid('^')
        self.assertFalse(result, "Should be False")


if __name__ == '__main__':
    unittest.main()
