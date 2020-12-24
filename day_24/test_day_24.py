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


if __name__ == "__main__":
    unittest.main()
