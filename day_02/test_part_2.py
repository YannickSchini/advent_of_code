import unittest
import day_02_part_2

class TestDay2(unittest.TestCase):


    def test_read_input(self):
       # Given
       list_of_test_lines = ["1-3 a: abcde",
                             "1-3 b: cdefg",
                             "2-9 c: ccccccccc"]

       # When
       input_text = day_02_part_2.load_file('test_file.txt')

       # Then
       self.assertEqual(input_text, list_of_test_lines)

    def test_parse_entry(self):
        # Given
        entry = "1-3 a: abcde"

        # When
        policy, password = day_02_part_2.parse_entry(entry)

        # Then
        self.assertEqual(policy, ((1, 3), "a"))
        self.assertEqual(password, "abcde")

    def test_check_if_passport_is_valid_return_true_with_valid_passport(self):
        # Given
        policy = ((1, 3), "a")
        password = "abcde"

        # When

        # Then
        self.assertTrue(day_02_part_2.check_if_passport_is_valid(policy, password))

    def test_check_if_passport_is_valid_return_false_with_password_with_no_letter(self):
        # Given
        policy = ((1, 3), "b")
        password = "cdefg"

        # When

        # Then
        self.assertFalse(day_02_part_2.check_if_passport_is_valid(policy, password))

    def test_check_if_passport_is_valid_return_false_with_password_with_too_many_letters(self):
        # Given
        policy = ((2, 9), "c")
        password = "ccccccccc"

        # When

        # Then
        self.assertFalse(day_02_part_2.check_if_passport_is_valid(policy, password))
if __name__ == "__main__":
    unittest.main()
