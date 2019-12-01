import unittest

from happy_num import is_first_iteration, square_sum, get_dist_happy, is_happy


class TestHappyNum(unittest.TestCase):
    def test_is_first_iteration(self):
        self.assertTrue(is_first_iteration(1))
        self.assertTrue(is_first_iteration(1234))
        self.assertFalse(is_first_iteration(1230))
        self.assertFalse(is_first_iteration(1243))

    def test_square_sum(self):
        self.assertEqual(1, square_sum(1))
        self.assertEqual(5, square_sum(12))
        self.assertEqual(20, square_sum(204))

    def test_is_happy(self):
        self.assertFalse(is_happy(89))
        self.assertTrue(is_happy(1))
        self.assertTrue(is_happy(10))

    def test_get_dist_happy(self):
        self.assertEqual(711, get_dist_happy(1000000))


if __name__ == '__main__':
    unittest.main()
