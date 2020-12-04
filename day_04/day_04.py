import re


class passport_validator():
    def __init__(self, file_path):
        with open(file_path, "r") as passport_file:
            self.unprocessed_passport_string = passport_file.read()
            self.unprocessed_passport_list = self.unprocessed_passport_string.split(
                '\n\n')
            self.passport_list = self._process_passport_list()
            self.mandatory_keys = {
                "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
            }

    def _process_passport_list(self):
        passport_list = []
        for unprocessed_passport in self.unprocessed_passport_list:
            passport = {}
            for passport_entry in re.split('\\n| ',
                                           unprocessed_passport.rstrip('\n')):
                key, value = passport_entry.split(':')
                passport[key] = value
            passport_list.append(passport)
        return passport_list

    def validate_passports(self):
        validation_list = self._check_all_mandatory_keys_are_present()
        return validation_list

    def _check_all_mandatory_keys_are_present(self):
        validation_list = []
        for passport in self.passport_list:
            if self.mandatory_keys.issubset(set(passport.keys())):
                validation_list.append(True)
            else:
                validation_list.append(False)
        return validation_list


if __name__ == "__main__":
    pass_val = passport_validator('input_file.txt')
    validations = pass_val.validate_passports()
    print(validations)
    print(sum(validations))
