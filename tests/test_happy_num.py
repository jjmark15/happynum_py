import unittest

from happy_num import is_first_iteration


class TestHappyNum(unittest.TestCase):
    def test_is_first_iteration(self):
        self.assertTrue(is_first_iteration(1))
        self.assertTrue(is_first_iteration(1234))


if __name__ == '__main__':
    unittest.main()
