import unittest
import day_19


class testDay19(unittest.TestCase):
    def test_create_regex_rule(self):
        # Given
        test = day_19.communicationFixer("test_file.txt")
        # When
        result = test.part_1()
        # Then
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
