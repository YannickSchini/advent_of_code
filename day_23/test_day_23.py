import unittest
import day_23


class testDay23(unittest.TestCase):
    def test_part_1(self):
        # Given
        input_cup_labeling = "389125467"
        # When
        result = day_23.part_1(input_cup_labeling)
        # Then
        self.assertEqual(result, "67384529")


if __name__ == "__main__":
    unittest.main()
