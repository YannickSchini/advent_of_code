import unittest
import day_05


class PassportValidatorTest(unittest.TestCase):
    def test_get_row(self):
        # Given
        boarding_pass_1 = "FBFBBFFRLR"
        boarding_pass_2 = "BFFFBBFRRR"
        boarding_pass_3 = "FFFBBBFRRR"
        boarding_pass_4 = "BBFFBBFRLL"
        # When
        row_1 = day_05.get_row(boarding_pass_1)
        row_2 = day_05.get_row(boarding_pass_2)
        row_3 = day_05.get_row(boarding_pass_3)
        row_4 = day_05.get_row(boarding_pass_4)
        # Then
        self.assertEqual(row_1, 44)
        self.assertEqual(row_2, 70)
        self.assertEqual(row_3, 14)
        self.assertEqual(row_4, 102)

    def test_get_column(self):
        # Given
        boarding_pass_1 = "FBFBBFFRLR"
        boarding_pass_2 = "BFFFBBFRRR"
        boarding_pass_3 = "FFFBBBFRRR"
        boarding_pass_4 = "BBFFBBFRLL"
        # When
        column_1 = day_05.get_column(boarding_pass_1)
        column_2 = day_05.get_column(boarding_pass_2)
        column_3 = day_05.get_column(boarding_pass_3)
        column_4 = day_05.get_column(boarding_pass_4)
        # Then
        self.assertEqual(column_1, 5)
        self.assertEqual(column_2, 7)
        self.assertEqual(column_3, 7)
        self.assertEqual(column_4, 4)

    def test_get_id(self):
        # Given
        boarding_pass_1 = "FBFBBFFRLR"
        boarding_pass_2 = "BFFFBBFRRR"
        boarding_pass_3 = "FFFBBBFRRR"
        boarding_pass_4 = "BBFFBBFRLL"
        # When
        id_1 = day_05.get_id(boarding_pass_1)
        id_2 = day_05.get_id(boarding_pass_2)
        id_3 = day_05.get_id(boarding_pass_3)
        id_4 = day_05.get_id(boarding_pass_4)
        # Then
        self.assertEqual(id_1, 357)
        self.assertEqual(id_2, 567)
        self.assertEqual(id_3, 119)
        self.assertEqual(id_4, 820)


if __name__ == "__main__":
    unittest.main()
