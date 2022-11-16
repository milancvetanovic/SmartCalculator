import unittest
from check_validity import check_brackets


class TestCheckBrackets(unittest.TestCase):
    def test_string(self):
        input_string = '((10+10)+10)+10'
        result = check_brackets(input_string)
        self.assertTrue(result, "Should be True")

    def test_missing_closing_bracket(self):
        input_string = '((10+10)+10+10'
        result = check_brackets(input_string)
        self.assertFalse(result, "Should be False")

    def test_missing_opening_bracket(self):
        input_string = '(10+10)+10)+10'
        result = check_brackets(input_string)
        self.assertFalse(result, "Should be False")

    def test_extra_opening_bracket(self):
        input_string = '(((10+10)+10)+10'
        result = check_brackets(input_string)
        self.assertFalse(result, "Should be False")

    def test_extra_closing_bracket(self):
        input_string = '((10+10)+10))+10'
        result = check_brackets(input_string)
        self.assertFalse(result, "Should be False")

    def test_misplaced_brackets(self):
        input_string = ')10+10(+10+10'
        result = check_brackets(input_string)
        self.assertFalse(result, "Should be False")

    def test_bracket_series(self):
        input_string = '(((((((())))))))'
        result = check_brackets(input_string)
        self.assertTrue(result, "Should be True")


if __name__ == '__main__':
    unittest.main()
