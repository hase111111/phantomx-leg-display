
import unittest
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from designlab.triangle_checker import TriangleChecker

class TestTriangleChecker(unittest.TestCase):
    def setUp(self):
        self.triangle_checker = TriangleChecker()

    def test_can_make_triangle(self):
        self.assertTrue(self.triangle_checker.can_make_triangle(3, 4, 5))
        self.assertTrue(self.triangle_checker.can_make_triangle(3, 5, 4))
        self.assertTrue(self.triangle_checker.can_make_triangle(4, 3, 5))
        self.assertTrue(self.triangle_checker.can_make_triangle(4, 5, 3))
        self.assertTrue(self.triangle_checker.can_make_triangle(5, 3, 4))
        self.assertTrue(self.triangle_checker.can_make_triangle(5, 4, 3))

        self.assertFalse(self.triangle_checker.can_make_triangle(1, 1, 2))
        self.assertFalse(self.triangle_checker.can_make_triangle(1, 2, 1))
        self.assertFalse(self.triangle_checker.can_make_triangle(2, 1, 1))


if __name__ == '__main__':
    unittest.main()