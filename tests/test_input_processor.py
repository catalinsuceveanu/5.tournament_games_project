import input_processor
import unittest


class testInputProcessor(unittest.TestCase):
    def test_get_the_correct_input_for_no_of_teams(self):
        set_keyboard_input(["9", "7"])
        input_processor.get_the_correct_input_for_no_of_teams()
        expected_output = ">> 9 << is invalid. Please insert an evan positive number."


if __name__ == "__main__":
    unittest.main()
