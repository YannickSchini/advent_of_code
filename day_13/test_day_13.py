import unittest
import day_13


class testDay13(unittest.TestCase):
    def test_part_1(self):
        # Given
        expected_result = 295
        test_file_path = "test_file.txt"
        # When
        result = day_13.part_1(test_file_path)
        # Then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
