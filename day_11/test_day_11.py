import unittest
from day_11 import seatingArea


class testSeatingArea(unittest.TestCase):
    def test_floor_plan_is_read_correctly(self):
        # Given
        expected_floor_plan = [
            'L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL',
            'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL',
            'L.LLLLLL.L', 'L.LLLLL.LL'
        ]
        # When
        testArea = seatingArea("test_file.txt")
        # Then
        self.assertEqual(testArea.floor_plan, expected_floor_plan)

    def test_get_seat_value(self):
        # Given
        testArea = seatingArea("test_file.txt")
        empty_seat_coord = (0, 0)
        floor_coord = (2, 1)
        invalid_coord_1 = (-1, 2)
        invalid_coord_2 = (8, 11)
        # When
        empty_seat_value = testArea._get_seat_value(*empty_seat_coord)
        floor_value = testArea._get_seat_value(*floor_coord)
        error_value_1 = testArea._get_seat_value(*invalid_coord_1)
        error_value_2 = testArea._get_seat_value(*invalid_coord_2)
        # Then
        self.assertEqual(empty_seat_value, 'L')
        self.assertEqual(floor_value, '.')
        self.assertEqual(error_value_1, IndexError)
        self.assertEqual(error_value_2, IndexError)

    def test_update_seating_status_gives_correct_results(self):
        # Given
        testArea = seatingArea("test_file.txt")
        after_round_1 = seatingArea("part_1_after_round_1.txt")
        after_round_2 = seatingArea("part_1_after_round_2.txt")
        after_round_3 = seatingArea("part_1_after_round_3.txt")
        after_round_4 = seatingArea("part_1_after_round_4.txt")
        after_round_5 = seatingArea("part_1_after_round_5.txt")
        # When
        result_after_1_round = testArea.update_seating_status()
        testArea.seats = result_after_1_round
        result_after_2_round = testArea.update_seating_status()
        testArea.seats = result_after_2_round
        result_after_3_round = testArea.update_seating_status()
        testArea.seats = result_after_3_round
        result_after_4_round = testArea.update_seating_status()
        testArea.seats = result_after_4_round
        result_after_5_round = testArea.update_seating_status()
        testArea.seats = result_after_5_round
        # Then
        self.assertEqual(result_after_1_round, after_round_1.seats)
        self.assertEqual(result_after_2_round, after_round_2.seats)
        self.assertEqual(result_after_3_round, after_round_3.seats)
        self.assertEqual(result_after_4_round, after_round_4.seats)
        self.assertEqual(result_after_5_round, after_round_5.seats)

    def test_get_stabilised_occupied_seat_count_get_correct_value(self):
        # Given
        testArea = seatingArea("test_file.txt")
        # When
        result = testArea.get_stabilised_occupied_seat_count()
        # Then
        self.assertEqual(result, 37)


if __name__ == "__main__":
    unittest.main()
