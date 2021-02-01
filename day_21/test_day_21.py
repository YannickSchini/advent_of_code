import unittest
import day_21


class testDay21(unittest.TestCase):
    def test_part_1(self):
        # Given
        input_file = "test_file.txt"
        expected_result = 5
        # When
        actual_result = day_21.part_1(input_file)
        # Then
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
