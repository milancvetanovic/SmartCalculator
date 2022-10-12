import unittest
from check_validity import check_first_char


class TestCheckFirstChar(unittest.TestCase):
    def test_multiplication_operator(self):
        result = check_first_char('*')
        self.assertTrue(result, "Should be True")

    def test_dividing_operator(self):
        result = check_first_char('/')
        self.assertTrue(result, "Should be True")

    def test_closing_bracket(self):
        result = check_first_char(')')
        self.assertTrue(result, "Should be True")

    def test_power_operator(self):
        result = check_first_char('^')
        self.assertTrue(result, "Should be True")

    def test_digit(self):
        result = check_first_char('1')
        self.assertFalse(result, "Should be False")

    def test_letter(self):
        result = check_first_char('a')
        self.assertFalse(result, "Should be False")

    def test_plus_operator(self):
        result = check_first_char('+')
        self.assertFalse(result, "Should be False")

    def test_minus_operator(self):
        result = check_first_char('-')
        self.assertFalse(result, "Should be False")

    def test_open_bracket(self):
        result = check_first_char('(')
        self.assertFalse(result, "Should be False")


if __name__ == '__main__':
    unittest.main()
