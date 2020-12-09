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
        # When
        result = day_09.process_xmas_file(file_path=file_path, PREAMBLE_SIZE=5)
        # Then
        self.assertEqual(result, 127)


if __name__ == "__main__":
    unittest.main()
