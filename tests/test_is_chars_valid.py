import unittest

from check_validity import is_chars_valid


class TestIsCharsValid(unittest.TestCase):
    def test_letters(self):
        data = 'abcdefghijklmnopqrstuvwxyz'
        self.assertTrue(is_chars_valid(data), "Should be True")

    def test_digits(self):
        data = '1234567890'
        self.assertTrue(is_chars_valid(data), "Should be True")

    def test_operators(self):
        data = '+-*/ ()^'
        self.assertTrue(is_chars_valid(data), "Should be True")

    def test_empty_string(self):
        data = ''
        self.assertTrue(is_chars_valid(data), "Should be True")

    def test_valid_expression(self):
        data = '(12+20) * 10 - 22/2 '
        self.assertTrue(is_chars_valid(data), "Should be True")

    def test_invalid_expression(self):
        data = '(12+20) * 10. - 22/2'
        self.assertFalse(is_chars_valid(data), "Should be False")

    def test_invalid_expression_2(self):
        data = '(12?+20) * 10 - 22/2'
        self.assertFalse(is_chars_valid(data), "Should be False")


if __name__ == '__main__':
    unittest.main()
