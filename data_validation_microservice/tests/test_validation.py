import unittest
from app.validation import validate_data

class ValidationTestCase(unittest.TestCase):
    def test_valid_data(self):
        self.assertEqual(validate_data("Valid data"), [])

    def test_empty_data(self):
        self.assertEqual(validate_data(""), ["Data must be a non-empty string."])

    def test_long_data(self):
        long_data = "a" * 256
        self.assertEqual(validate_data(long_data), ["Data must be 255 characters or fewer."])

if __name__ == '__main__':
    unittest.main()
