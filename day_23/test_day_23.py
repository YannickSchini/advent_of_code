import unittest
import day_23


class testDay23(unittest.TestCase):
    def test_part_1(self):
        # Given
        input_cup_labeling = "389125467"
        # When
        result_after_10 = day_23.part_1(input_cup_labeling, 10)
        result_after_100 = day_23.part_1(input_cup_labeling, 100)
        # Then
        self.assertEqual(result_after_10, "92658374")
        self.assertEqual(result_after_100, "67384529")


if __name__ == "__main__":
    unittest.main()
