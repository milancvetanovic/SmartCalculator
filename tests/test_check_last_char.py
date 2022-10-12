import unittest
from check_validity import check_last_char


class TestCheckLastChar(unittest.TestCase):
    def test_plus_operator(self):
        result = check_last_char('+')
        self.assertTrue(result, "Should be True")

    def test_minus_operator(self):
        result = check_last_char('-')
        self.assertTrue(result, "Should be True")

    def test_multiplication_operator(self):
        result = check_last_char('*')
        self.assertTrue(result, "Should be True")

    def test_dividing_operator(self):
        result = check_last_char('/')
        self.assertTrue(result, "Should be True")

    def test_open_bracket(self):
        result = check_last_char('(')
        self.assertTrue(result, "Should be True")

    def test_power_operator(self):
        result = check_last_char('^')
        self.assertTrue(result, "Should be True")


if __name__ == '__main__':
    unittest.main()
