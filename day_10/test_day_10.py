import day_10
import unittest


class day10Test(unittest.TestCase):
    def test_part_1_on_example_files(self):
        # Given
        with open("test_file_small.txt", "r") as test_file_small:
            small_list_of_adapters = test_file_small.readlines()
        small_list_of_adapters = [int(x) for x in small_list_of_adapters]
        with open("test_file_large.txt", "r") as test_file_large:
            large_list_of_adapters = test_file_large.readlines()
        large_list_of_adapters = [int(x) for x in large_list_of_adapters]
        # When
        results_small = day_10.part_1(small_list_of_adapters)
        results_large = day_10.part_1(large_list_of_adapters)
        # Then
        self.assertEqual(results_small, 35)
        self.assertEqual(results_large, 220)

    def test_part_2_on_example_file(self):
        # Given
        with open("test_file_small.txt", "r") as test_file_small:
            small_list_of_adapters = test_file_small.readlines()
        small_list_of_adapters = [int(x) for x in small_list_of_adapters]
        with open("test_file_large.txt", "r") as test_file_large:
            large_list_of_adapters = test_file_large.readlines()
        large_list_of_adapters = [int(x) for x in large_list_of_adapters]
        # When
        results_small = day_10.part_2(small_list_of_adapters)
        results_large = day_10.part_2(large_list_of_adapters)
        # Then
        self.assertEqual(results_small, 8)
        self.assertEqual(results_large, 19208)


if __name__ == "__main__":
    unittest.main()
