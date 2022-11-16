import unittest

from check_validity import is_first_char_valid


class TestIsFirstCharValid(unittest.TestCase):
    def test_multiplication_operator(self):
        result = is_first_char_valid('*')
        self.assertFalse(result, "Should be False")

    def test_dividing_operator(self):
        result = is_first_char_valid('/')
        self.assertFalse(result, "Should be False")

    def test_closing_bracket(self):
        result = is_first_char_valid(')')
        self.assertFalse(result, "Should be False")

    def test_power_operator(self):
        result = is_first_char_valid('^')
        self.assertFalse(result, "Should be False")

    def test_digit(self):
        result = is_first_char_valid('1')
        self.assertTrue(result, "Should be True")

    def test_letter(self):
        result = is_first_char_valid('a')
        self.assertTrue(result, "Should be True")

    def test_plus_operator(self):
        result = is_first_char_valid('+')
        self.assertTrue(result, "Should be True")

    def test_minus_operator(self):
        result = is_first_char_valid('-')
        self.assertTrue(result, "Should be True")

    def test_open_bracket(self):
        result = is_first_char_valid('(')
        self.assertTrue(result, "Should be True")


if __name__ == '__main__':
    unittest.main()
