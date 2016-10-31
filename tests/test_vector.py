import unittest
import vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = vector.Vector([1, 2, 3])
        self.v2 = vector.Vector([2, 3, 4])
        self.c = 2

    def test_add(self):
        self.assertEqual(self.v1.add(self.v2), vector.Vector([3, 5, 7]))

    def test_subtract(self):
        self.assertEqual(self.v1.subtract(self.v2), vector.Vector([-1, -1, -1]))

    def test_multiply(self):
        self.assertEqual(self.v1.scalar_multiply(self.c), vector.Vector([2, 4, 6]))

    def test_magnitude(self):
        self.assertAlmostEqual(self.v1.magnitude(), 3.7416573867739413)

if __name__ == '__main__':
    unittest.main()
