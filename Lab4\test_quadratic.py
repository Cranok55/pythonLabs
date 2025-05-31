import unittest
from app import solve_quadratic  # если функция в app.py

class TestQuadraticSolver(unittest.TestCase):

    def test_two_roots(self):
        roots = solve_quadratic(1, -3, 2)
        self.assertEqual(set(roots), {2, 1})  # корни 1 и 2

    def test_one_root(self):
        roots = solve_quadratic(1, 2, 1)
        self.assertEqual(roots, (-1,))

    def test_no_roots(self):
        roots = solve_quadratic(1, 0, 1)
        self.assertEqual(roots, ())

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 1)

if __name__ == '__main__':
    unittest.main()
