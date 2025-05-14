import unittest
from src.randompkg import MYpRNG

class TestMYpRNG(unittest.TestCase):

    def test_seed_repeatability(self):
        MYpRNG.setSeed(10)
        a = MYpRNG.pRNG()
        MYpRNG.setSeed(10)
        b = MYpRNG.pRNG()
        self.assertEqual(a, b)

    def test_modulo_effect(self):
        MYpRNG.setSeed(5)
        MYpRNG.setMultiplier(3)
        MYpRNG.setIncrement(7)
        MYpRNG.setModulo(11)
        val = MYpRNG.pRNG()
        self.assertTrue(0 <= val < 11)

if __name__ == "__main__":
    unittest.main()