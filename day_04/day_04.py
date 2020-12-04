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
        validation_list = []
        for passport in self.passport_list:
            if self._check_all_mandatory_keys_are_present(passport) and \
            self._check_if_byr_is_valid(passport["byr"]) and \
            self._check_if_iyr_is_valid(passport["iyr"]) and \
            self._check_if_eyr_is_valid(passport["eyr"]) and \
            self._check_if_hgt_is_valid(passport["hgt"]) and \
            self._check_if_hcl_is_valid(passport["hcl"]) and \
            self._check_if_ecl_is_valid(passport["ecl"]) and \
            self._check_if_pid_is_valid(passport["pid"]):
                validation_list.append(True)
            else:
                validation_list.append(False)
        return validation_list

    def _check_all_mandatory_keys_are_present(self, passport):
        if self.mandatory_keys.issubset(set(passport.keys())):
            return True
        else:
            return False

    def _check_if_byr_is_valid(self, byr_value):
        try:
            byr = int(byr_value)
            if 1920 <= byr <= 2002:
                return True
        except ValueError:
            pass
        return False

    def _check_if_iyr_is_valid(self, iyr_value):
        try:
            iyr = int(iyr_value)
            if 2010 <= iyr <= 2020:
                return True
        except ValueError:
            pass
        return False

    def _check_if_eyr_is_valid(self, eyr_value):
        try:
            eyr = int(eyr_value)
            if 2020 <= eyr <= 2030:
                return True
        except ValueError:
            pass
        return False

    def _check_if_hgt_is_valid(self, hgt_value):
        hgt_unit = hgt_value[-2:]
        hgt_numerical = hgt_value[:-2]
        try:
            hgt = int(hgt_numerical)
        except ValueError:
            return False
        if hgt_unit == "in":
            if 59 <= hgt <= 76:
                return True
        if hgt_unit == "cm":
            if 150 <= hgt <= 193:
                return True
        return False

    def _check_if_hcl_is_valid(self, hcl_value):
        if re.match("^#[0-9a-f]{6}", hcl_value) is not None:
            return True
        return False

    def _check_if_ecl_is_valid(self, ecl_value):
        return (ecl_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

    def _check_if_pid_is_valid(self, pid_value):
        if re.match("^[0-9]{9}$", pid_value) is not None:
            return True
        return False


if __name__ == "__main__":
    pass_val = passport_validator('input_file.txt')
    validations = pass_val.validate_passports()
    print(validations)
    print(sum(validations))
