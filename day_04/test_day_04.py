import unittest
from day_04 import passport_validator


class PassportValidatorTest(unittest.TestCase):
    def test_opening_files_returns_string(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        # When

        # Then
        self.assertEqual(type(pass_val.unprocessed_passport_string), str)

    def test_unprocessed_passport_list_gets_the_right_number_of_passports(
            self):
        # Given
        pass_val = passport_validator('test_file.txt')
        # When

        # Then
        self.assertEqual(len(pass_val.unprocessed_passport_list), 4)

    def test_process_passport_list_returns_correct_list_of_dicts(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        expected_passports = [{
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm"
        }, {
            "iyr": "2013",
            "ecl": "amb",
            "cid": "350",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929"
        }, {
            "hcl": "#ae17e1",
            "iyr": "2013",
            "eyr": "2024",
            "ecl": "brn",
            "pid": "760753108",
            "byr": "1931",
            "hgt": "179cm"
        }, {
            "hcl": "#cfa07d",
            "eyr": "2025",
            "pid": "166559648",
            "iyr": "2011",
            "ecl": "brn",
            "hgt": "59in"
        }]
        # When

        # Then
        self.assertEqual(pass_val.passport_list, expected_passports)

    def test_validate_passports_on_example_data(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        # When
        validations = pass_val.validate_passports()
        # Then
        self.assertEqual(sum(validations), 2)

    def test_check_if_byr_is_valid(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        valid_byr = 2002
        invalid_byr = 2003
        # When
        valid_result = pass_val._check_if_byr_is_valid(valid_byr)
        invalid_result = pass_val._check_if_byr_is_valid(invalid_byr)
        # Then
        self.assertTrue(valid_result)
        self.assertFalse(invalid_result)

    def test_check_if_iyr_is_valid(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        valid_iyr = 2012
        invalid_iyr = 2023
        # When
        valid_result = pass_val._check_if_iyr_is_valid(valid_iyr)
        invalid_result = pass_val._check_if_iyr_is_valid(invalid_iyr)
        # Then
        self.assertTrue(valid_result)
        self.assertFalse(invalid_result)

    def test_check_if_eyr_is_valid(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        valid_eyr = 2022
        invalid_eyr = 2013
        # When
        valid_result = pass_val._check_if_eyr_is_valid(valid_eyr)
        invalid_result = pass_val._check_if_eyr_is_valid(invalid_eyr)
        # Then
        self.assertTrue(valid_result)
        self.assertFalse(invalid_result)

    def test_check_if_hgt_is_valid(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        valid_hgt_1 = "60in"
        valid_hgt_2 = "190cm"
        invalid_hgt_1 = "190in"
        invalid_hgt_2 = 190
        # When
        valid_result_1 = pass_val._check_if_hgt_is_valid(valid_hgt_1)
        valid_result_2 = pass_val._check_if_hgt_is_valid(valid_hgt_2)
        invalid_result_1 = pass_val._check_if_eyr_is_valid(invalid_hgt_1)
        invalid_result_2 = pass_val._check_if_eyr_is_valid(invalid_hgt_2)
        # Then
        self.assertTrue(valid_result_1)
        self.assertTrue(valid_result_2)
        self.assertFalse(invalid_result_1)
        self.assertFalse(invalid_result_2)

    def test_check_if_hcl_is_valid(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        valid_hcl = '#123abc'
        invalid_hcl_1 = '#123abz'
        invalid_hcl_2 = '123abc'
        # When
        valid_result = pass_val._check_if_hcl_is_valid(valid_hcl)
        invalid_result_1 = pass_val._check_if_hcl_is_valid(invalid_hcl_1)
        invalid_result_2 = pass_val._check_if_hcl_is_valid(invalid_hcl_2)
        # Then
        self.assertTrue(valid_result)
        self.assertFalse(invalid_result_1)
        self.assertFalse(invalid_result_2)

    def test_check_if_ecl_is_valid(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        valid_ecl = 'brn'
        invalid_ecl = 'wat'
        # When
        valid_result = pass_val._check_if_ecl_is_valid(valid_ecl)
        invalid_result = pass_val._check_if_ecl_is_valid(invalid_ecl)
        # Then
        self.assertTrue(valid_result)
        self.assertFalse(invalid_result)

    def test_check_if_pid_is_valid(self):
        # Given
        pass_val = passport_validator('test_file.txt')
        valid_pid = '000000001'
        invalid_pid = '0123456789'
        # When
        valid_result = pass_val._check_if_pid_is_valid(valid_pid)
        invalid_result = pass_val._check_if_pid_is_valid(invalid_pid)
        # Then
        self.assertTrue(valid_result)
        self.assertFalse(invalid_result)


if __name__ == "__main__":
    unittest.main()
