import unittest
from src.randompkg import MYProbability

class TestMYProbability(unittest.TestCase):

    def test_uniform(self):
        for _ in range(10):
            val = MYProbability.uniform(5, 10)
            self.assertTrue(5 <= val <= 10)

    def test_bernoulli(self):
        val = MYProbability.bernoulli(0.7)
        self.assertIn(val, [0, 1])

    def test_binomial(self):
        val = MYProbability.binomial(10, 0.5)
        self.assertTrue(0 <= val <= 10)

    def test_gaussian(self):
        val = MYProbability.gaussian(0, 1)
        self.assertIsInstance(val, float)

    def test_poisson(self):
        val = MYProbability.poisson(5)
        self.assertTrue(val >= 0)

if __name__ == "__main__":
    unittest.main()
