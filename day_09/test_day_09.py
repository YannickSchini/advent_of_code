import unittest
import day_09


class testDay08(unittest.TestCase):
    def test_can_number_be_decomposed(self):
        # Given
        number_true = 25
        number_false = 22
        number_list = [10, 11, 13, 14, 15, 16, 17]
        # When
        expect_true = day_09.can_number_be_decomposed(number_true, number_list)
        expect_false = day_09.can_number_be_decomposed(number_false,
                                                       number_list)
        # Then
        self.assertTrue(expect_true)
        self.assertFalse(expect_false)

    def test_process_xmas_file(self):
        # Given
        file_path = "test_file.txt"
        with open(file_path, "r") as xmas_input:
            number_list = xmas_input.readlines()
            number_list = [int(x) for x in number_list]
        # When
        result = day_09.process_xmas_file(number_list=number_list,
                                          PREAMBLE_SIZE=5)
        # Then
        self.assertEqual(result, 127)

    def test_find_sublist_that_sums_to_number(self):
        # Given
        number_1 = 35
        number_list_1 = [10, 12, 13, 45, 50]
        sublist_1 = [10, 12, 13]
        number_2 = 85
        number_list_2 = [10, 11, 13, 12, 40, 20, 100]
        sublist_2 = [13, 12, 40, 20]
        # When
        result_1 = day_09.find_sublist_that_sums_to_number(
            number_1, number_list_1)
        result_2 = day_09.find_sublist_that_sums_to_number(
            number_2, number_list_2)
        # Then
        self.assertEqual(result_1, sublist_1)
        self.assertEqual(result_2, sublist_2)


if __name__ == "__main__":
    unittest.main()
