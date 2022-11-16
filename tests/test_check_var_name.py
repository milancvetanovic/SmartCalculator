import unittest
from check_validity import check_var_name


class TestCheckVarName(unittest.TestCase):
    def test_letters(self):
        result = check_var_name('cups')
        self.assertTrue(result, "Should be True")

    def test_digit_first(self):
        result = check_var_name('9cups')
        self.assertFalse(result, "Should be False")

    def test_digit_middle(self):
        result = check_var_name('cu7ps')
        self.assertTrue(result, "Should be True")

    def test_digit_end(self):
        result = check_var_name('cups10')
        self.assertTrue(result, "Should be True")

    def test_uppercase_letters(self):
        result = check_var_name('CUPS')
        self.assertTrue(result, "Should be True")

    def test_underscore(self):
        result = check_var_name('cups_9')
        self.assertFalse(result, "Should be False")

    def test_dot(self):
        result = check_var_name('cups.9')
        self.assertFalse(result, "Should be False")


if __name__ == '__main__':
    unittest.main()
