import unittest
import day_17


class testDay17(unittest.TestCase):
    def test_part_1(self):
        # Given
        expected_result = 112
        test_file = "test_file.txt"
        # When
        result = day_17.part_1(test_file)
        # Then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
