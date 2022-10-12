import unittest
from check_validity import check_var_name


class TestCheckVarName(unittest.TestCase):
    def test_letters(self):
        result = check_var_name('cups')
        self.assertFalse(result, "Should be False")

    def test_digit_first(self):
        result = check_var_name('9cups')
        self.assertTrue(result, "Should be True")

    def test_digit_middle(self):
        result = check_var_name('cu7ps')
        self.assertFalse(result, "Should be False")

    def test_digit_end(self):
        result = check_var_name('cups10')
        self.assertFalse(result, "Should be False")

    def test_uppercase_letters(self):
        result = check_var_name('CUPS')
        self.assertFalse(result, "Should be False")

    def test_underscore(self):
        result = check_var_name('cups_9')
        self.assertTrue(result, "Should be True")

    def test_dot(self):
        result = check_var_name('cups.9')
        self.assertTrue(result, "Should be True")


if __name__ == '__main__':
    unittest.main()
