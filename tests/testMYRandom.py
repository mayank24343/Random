import unittest
from src.randompkg import MYRandom

class TestMYRandom(unittest.TestCase):
    def test_random_range(self):
        for _ in range(10):
            val = MYRandom.random()
            self.assertTrue(0 <= val < 1)

    def test_randint(self):
        for _ in range(10):
            val = MYRandom.randint(5, 10)
            self.assertTrue(5 <= val <= 10)

    def test_choice_single(self):
        self.assertIn(MYRandom.choice([1, 2, 3]), [1, 2, 3])

    def test_shuffle(self):
        original = [1, 2, 3, 4, 5]
        shuffled = original[:]
        MYRandom.shuffle(shuffled)
        self.assertEqual(sorted(shuffled), sorted(original))

if __name__ == "__main__":
    unittest.main()
