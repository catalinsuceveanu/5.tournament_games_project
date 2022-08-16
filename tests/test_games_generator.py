import games_generator
import unittest
from unittest import mock


class testGamesGenerator(unittest.TestCase):
    def testGenerate_games(self):
        test_1 = {"ghosts": 2, "sharks": 4}
        result_1 = [["ghosts", "sharks"]]

        test_2 = {
            "ghosts": 2,
            "sharks": 4,
            "stars": 0,
            "brains": 9,
            "wolfs": 1,
            "eagles": 3,
        }
        result_2 = [["stars", "brains"], ["wolfs", "sharks"], ["ghosts", "eagles"]]

        test_3 = {}
        result_3 = []

        self.assertEqual(games_generator.generate_games(test_1), result_1)
        self.assertEqual(games_generator.generate_games(test_2), result_2)
        self.assertEqual(games_generator.generate_games(test_3), result_3)


if __name__ == "__main__":
    unittest.main()
