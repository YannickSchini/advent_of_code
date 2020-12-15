import unittest
import day_15


class testDay15(unittest.TestCase):
    def test_part_1(self):
        # Given
        starting_1 = [0, 3, 6]
        starting_2 = [1, 3, 2]
        starting_3 = [2, 1, 3]
        starting_4 = [1, 2, 3]
        starting_5 = [2, 3, 1]
        starting_6 = [3, 2, 1]
        starting_7 = [3, 1, 2]
        # When
        result_1 = day_15.day_15_test(starting_1, 2020)
        result_2 = day_15.day_15_test(starting_2, 2020)
        result_3 = day_15.day_15_test(starting_3, 2020)
        result_4 = day_15.day_15_test(starting_4, 2020)
        result_5 = day_15.day_15_test(starting_5, 2020)
        result_6 = day_15.day_15_test(starting_6, 2020)
        result_7 = day_15.day_15_test(starting_7, 2020)
        # Then
        self.assertEqual(result_1, 436)
        self.assertEqual(result_2, 1)
        self.assertEqual(result_3, 10)
        self.assertEqual(result_4, 27)
        self.assertEqual(result_5, 78)
        self.assertEqual(result_6, 438)
        self.assertEqual(result_7, 1836)

    def test_part_2(self):
        # Given
        starting_1 = [0, 3, 6]
        starting_2 = [1, 3, 2]
        starting_3 = [2, 1, 3]
        starting_4 = [1, 2, 3]
        starting_5 = [2, 3, 1]
        starting_6 = [3, 2, 1]
        starting_7 = [3, 1, 2]
        # When
        result_1 = day_15.day_15_test(starting_1, 30000000)
        result_2 = day_15.day_15_test(starting_2, 30000000)
        result_3 = day_15.day_15_test(starting_3, 30000000)
        result_4 = day_15.day_15_test(starting_4, 30000000)
        result_5 = day_15.day_15_test(starting_5, 30000000)
        result_6 = day_15.day_15_test(starting_6, 30000000)
        result_7 = day_15.day_15_test(starting_7, 30000000)
        # Then
        self.assertEqual(result_1, 436)
        self.assertEqual(result_2, 1)
        self.assertEqual(result_3, 10)
        self.assertEqual(result_4, 27)
        self.assertEqual(result_5, 78)
        self.assertEqual(result_6, 438)
        self.assertEqual(result_7, 1836)


if __name__ == "__main__":
    unittest.main()
