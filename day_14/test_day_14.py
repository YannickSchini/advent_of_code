import unittest
import day_14


class testDay14(unittest.TestCase):
    def test_part_1(self):
        # Given
        input_filepath = "test_file.txt"
        expected_result = 165
        # When
        result = day_14.part_1(input_filepath)
        # Then
        self.assertEqual(result, expected_result)

    def test_apply_mask(self):
        # Given
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        test_value_1 = 11
        test_value_2 = 101
        test_value_3 = 0
        expected_result_1 = 73
        expected_result_2 = 101
        expected_result_3 = 64
        # When
        result_1 = day_14.apply_mask(test_value_1, mask)
        result_2 = day_14.apply_mask(test_value_2, mask)
        result_3 = day_14.apply_mask(test_value_3, mask)
        # Then
        self.assertEqual(result_1, expected_result_1)
        self.assertEqual(result_2, expected_result_2)
        self.assertEqual(result_3, expected_result_3)


if __name__ == "__main__":
    unittest.main()
