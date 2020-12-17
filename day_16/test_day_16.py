import unittest
import day_16


class testDay16(unittest.TestCase):
    def test_parse_file(self):
        # Given
        file_path = "test_file_part_1.txt"
        expected_rules = {
            "class": list(range(1, 4)) + list(range(5, 8)),
            "row": list(range(6, 12)) + list(range(33, 45)),
            "seat": list(range(13, 41)) + list(range(45, 51))
        }
        expected_ticket = [7, 1, 14]
        expected_nearby_tickets = [[7, 3, 47], [40, 4, 50], [55, 2, 20],
                                   [38, 6, 12]]
        # When
        rules, your_ticket, nearby_tickets = day_16.parse_file(file_path)
        # Then
        self.assertEqual(rules, expected_rules)
        self.assertEqual(your_ticket, expected_ticket)
        self.assertEqual(expected_nearby_tickets, nearby_tickets)

    def test_part_1(self):
        # Given
        expected_result = 71
        test_file = "test_file_part_1.txt"
        # When
        result = day_16.part_1(test_file)
        # Then
        self.assertEqual(result, expected_result)

    def test_get_invalid_value_of_ticket(self):
        # Given
        valid_ticket = [2, 12, 21]
        invalid_ticket_1 = [1, 10, 13]
        invalid_ticket_2 = [4, 9, 23]
        rules = {
            "toto": [1, 2, 3, 5, 6],
            "tata": [10, 11, 12, 14, 15, 16],
            "titi": [20, 21, 22]
        }
        # When
        valid_result = day_16.get_invalid_value(valid_ticket, rules)
        invalid_result_1 = day_16.get_invalid_value(invalid_ticket_1, rules)
        invalid_result_2 = day_16.get_invalid_value(invalid_ticket_2, rules)
        # Then
        self.assertEqual(valid_result, None)
        self.assertEqual(invalid_result_1, 13)
        self.assertEqual(invalid_result_2, 4)

    def test_part_2(self):
        # Given
        expected_result = {0: "row", 1: "class", 2: "seat"}
        test_file = "test_file_part_2.txt"
        # When
        result = day_16.part_2(test_file)
        # Then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
