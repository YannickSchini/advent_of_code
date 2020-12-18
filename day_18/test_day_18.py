import unittest
import day_18


class testDay18(unittest.TestCase):
    def test_part_1(self):
        # Given
        test_file = "test_file.txt"
        expected_result = 71 + 51 + 26 + 437 + 12240 + 13632
        # When
        result = day_18.part_1(test_file)
        # Then
        self.assertEqual(result, expected_result)

    def test_evaluate_expression_without_parenthesis(self):
        # Given
        input_string_1 = "1 + 2 * 3 + 4 * 5 + 6"
        expected_result_1 = 71
        input_string_2 = "2 + 3 * 2"
        expected_result_2 = 10
        # When
        result_1 = day_18.evaluate_expression_without_parenthesis(
            input_string_1)
        result_2 = day_18.evaluate_expression_without_parenthesis(
            input_string_2)
        # Then
        self.assertEqual(expected_result_1, result_1)
        self.assertEqual(expected_result_2, result_2)

    def test_replace_first_inner_parenthesis(self):
        # Given
        input_string_1 = "1 + 2 + 3"
        expected_result_1 = "1 + 2 + 3"
        input_string_2 = "1 + 2 + (2 * 3 + 5)"
        expected_result_2 = "1 + 2 + 11"
        input_string_3 = "1 + 2 + (2 * 3) + (2 * 3)"
        expected_result_3 = "1 + 2 + 6 + (2 * 3)"
        input_string_4 = "1 + (((2 + 3) * 4) + 1) + (2 * 3)"
        expected_result_4 = "1 + ((5 * 4) + 1) + (2 * 3)"
        # When
        result_1 = day_18.replace_first_inner_parenthesis(input_string_1)
        result_2 = day_18.replace_first_inner_parenthesis(input_string_2)
        result_3 = day_18.replace_first_inner_parenthesis(input_string_3)
        result_4 = day_18.replace_first_inner_parenthesis(input_string_4)
        # Then
        self.assertEqual(result_1, expected_result_1)
        self.assertEqual(result_2, expected_result_2)
        self.assertEqual(result_3, expected_result_3)
        self.assertEqual(result_4, expected_result_4)


if __name__ == "__main__":
    unittest.main()
