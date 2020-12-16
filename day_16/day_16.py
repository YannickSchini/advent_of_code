import re
from typing import Dict, List


def parse_file(file_path: str) -> (Dict[str, int], List[int], List[List[int]]):
    with open(file_path, "r") as input_file:
        full_text = input_file.read()
    rule_string, own_ticket_string, other_tickets_string = full_text.split(
        '\n\n')
    rule_dict = {}
    for rule in rule_string.split("\n"):
        numbers = [int(x) for x in re.findall("\d+", rule)]
        if len(numbers) != 4:
            raise ValueError
        rule_dict[rule.split(":")[0]] = list(range(
            numbers[0], numbers[1] + 1)) + list(
                range(numbers[2], numbers[3] + 1))
    ticket = own_ticket_string.split("\n")[1]
    other_tickets = other_tickets_string.split("\n")[1:-1]
    return rule_dict, [int(x) for x in ticket.split(",")
                       ], [[int(x) for x in other_ticket.split(",")]
                           for other_ticket in other_tickets]


def part_1(file_path: str) -> int:
    rules, ticket, other_tickets = parse_file(file_path)
    invalid_values = []
    for other_ticket in other_tickets:
        invalid_values.append(get_invalid_value(other_ticket, rules))
    return sum(invalid_values)


def get_invalid_value(ticket, rules):
    for value in ticket:
        is_value_valid = []
        for field in rules.keys():
            if value not in rules[field]:
                is_value_valid.append(False)
            else:
                is_value_valid.append(True)
        if True not in is_value_valid:
            return value
    return 0


if __name__ == "__main__":
    print("Part 1: ", part_1("input_file.txt"))
