from countries import get_country_code
import unittest

class TestModule(unittest.TestCase):
    def test_get_code(self):
        code = get_country_code("United Kingdom")
        self.assertEqual(code, "gb")


if __name__ == '__main__':
    unittest.main()