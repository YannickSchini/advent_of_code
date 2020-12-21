from typing import Dict, List
import re


class communicationFixer:
    def __init__(self, file_path):
        self.messages, self.rule_dict = self.parse_input(file_path)

    def parse_input(self, file_path):
        with open(file_path, "r") as input_file:
            full_text = input_file.read()
            rule_string, received_message_string = full_text.split('\n\n')
            rules = rule_string.split("\n")
            messages = received_message_string.split("\n")[:-1]
            rule_dict = {}
            for rule in rules:
                key, value = rule.split(":")
                rule_dict[int(key)] = value
            return messages, rule_dict

    def create_regex(self, key: int) -> str:
        rule_value = self.rule_dict[key]
        if key == 8:
            return self.create_regex(42) + "{1,5}"
        if key == 11:
            one_repeat = "".join(
                [self.create_regex(42),
                 self.create_regex(31)])
            two_repeat = "".join([
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(31),
                self.create_regex(31)
            ])
            three_repeat = "".join([
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(31),
                self.create_regex(31),
                self.create_regex(31)
            ])
            four_repeat = "".join([
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(31),
                self.create_regex(31),
                self.create_regex(31),
                self.create_regex(31)
            ])
            five_repeat = "".join([
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(42),
                self.create_regex(31),
                self.create_regex(31),
                self.create_regex(31),
                self.create_regex(31),
                self.create_regex(31)
            ])
            return "(" + "|".join([
                one_repeat, two_repeat, three_repeat, four_repeat, five_repeat
            ]) + ")"
        if "\"" in rule_value:
            return rule_value[2]
        elif re.match("^( \d+)+$", rule_value):
            return ''.join([
                self.create_regex(int(x))
                for x in rule_value.strip(" ").split(' ')
            ])
        elif "|" in rule_value:
            return "(" + ''.join([
                self.create_regex(int(x))
                for x in rule_value.split("|")[0].strip(" ").split(' ')
            ]) + "|" + ''.join([
                self.create_regex(int(x))
                for x in rule_value.split("|")[1].strip(" ").split(' ')
            ]) + ")"
        else:
            raise ValueError

    def part_1(self):
        regex_string = self.create_regex(0)
        counter = 0
        for message in self.messages:
            if re.match("^" + regex_string + "$", message):
                counter += 1
            else:
                pass
        return counter


if __name__ == "__main__":
    test = communicationFixer("input_file.txt")
    print(test.part_1())
