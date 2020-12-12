import unittest
import day_12


class testDay12(unittest.TestCase):
    def test_part_1(self):
        # Given
        testShip = day_12.Ship_part_1("test_file.txt")
        testShip.make_all_moves()
        # When
        distance = testShip.calculate_distance()
        # Then
        self.assertEqual(25, distance)


if __name__ == "__main__":
    unittest.main()
