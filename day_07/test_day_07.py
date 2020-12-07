import unittest
from day_07_part_1 import bagRules as bagRules_1
from day_07_part_2 import bagRules as bagRules_2


class testBagRules_1(unittest.TestCase):
    def test_shiny_gold_rule(self):
        # Given
        tested_object = bagRules_1('test_file_part_1.txt')
        # When
        results = tested_object.get_available_options()
        # Then
        self.assertEqual(len(results), 4)


class testBagRules_2(unittest.TestCase):
    def test_shiny_gold_rule(self):
        # Given
        tested_object = bagRules_2('test_file_part_2.txt')
        # When
        results = tested_object.get_count_inside_bag("shiny gold")
        # Then
        self.assertEqual(results, 126)


if __name__ == "__main__":
    unittest.main()
