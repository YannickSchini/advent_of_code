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


if __name__ == "__main__":
    unittest.main()
