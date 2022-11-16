import unittest

from check_validity import is_chars_valid


class TestIsCharsValid(unittest.TestCase):
    def test_letters(self):
        data = 'abcdefghijklmnopqrstuvwxyz'
        self.assertTrue(is_chars_valid(data), "Should be True")

    def test_digits(self):
        data = '1234567890'
        self.assertTrue(is_chars_valid(data), "Should be True")


if __name__ == '__main__':
    unittest.main()
