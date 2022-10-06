import unittest
from check_validity import invalid_chars


class TestInvalidChars(unittest.TestCase):
    def test_string_letters(self):
        input_string = 'abcdefghijklmnopqrstuvwxvz'
        result = invalid_chars(input_string)
        self.assertFalse(result, "Should be False")

    def test_string_digits(self):
        input_string = '1234567890'
        result = invalid_chars(input_string)
        self.assertFalse(result, "Should be False")

    def test_string_operators(self):
        input_string = '+-*/ ()^'
        result = invalid_chars(input_string)
        self.assertFalse(result, "Should be False")

    def test_empty_string(self):
        input_string = ''
        result = invalid_chars(input_string)
        self.assertFalse(result, "Should be False")

    def test_valid_expression(self):
        input_string = '(12+20) * 10 - 22/2 '
        result = invalid_chars(input_string)
        self.assertFalse(result, "Should be False")

    def test_invalid_expression(self):
        input_string = '(12+20) * 10. - 22/2'
        result = invalid_chars(input_string)
        self.assertTrue(result, "Should be True")

    def test_invalid_expression_2(self):
        input_string = '(12?+20) * 10 - 22/2'
        result = invalid_chars(input_string)
        self.assertTrue(result, "Should be True")


if __name__ == '__main__':
    unittest.main()
