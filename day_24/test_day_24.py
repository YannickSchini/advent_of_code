import unittest
import day_24


class testDay24(unittest.TestCase):
    def test_part_1(self):
        # Given
        file_path = "test_file.txt"
        # When
        result = day_24.part_1(file_path)
        # Then
        self.assertEqual(result, 10)

    def test_part_2(self):
        # Given
        file_path = "test_file.txt"
        # When
        result = day_24.part_2(file_path)
        # Then
        self.assertEqual(result, 2208)


if __name__ == "__main__":
    unittest.main()
