import re
from typing import Dict, List


def parse_file(
        file_path: str) -> (Dict[str, List[int]], List[int], List[List[int]]):
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
    return sum([i for i in invalid_values if i])


def part_2(file_path: str) -> int:
    rules, ticket, other_tickets = parse_file(file_path)
    valid_tickets = discard_invalid_tickets(other_tickets, rules)
    matching_fields_dict = build_matching_fields_dict(valid_tickets, rules)
    position_of_fields = get_final_fields_dict(matching_fields_dict)
    position_of_fields = {v: k for k, v in position_of_fields.items()}
    product = 1
    for key in position_of_fields:
        if key[:9] == "departure":
            product *= ticket[position_of_fields[key]]
    return product


def build_matching_fields_dict(
        tickets: List[List[int]],
        rules: Dict[str, List[int]]) -> Dict[int, List[str]]:
    matching_fields_dict = {}
    for index in range(len(tickets[0])):
        matching_fields_dict[index] = []
        for field in rules.keys():
            if all(ticket[index] in rules[field] for ticket in tickets):
                matching_fields_dict[index].append(field)
    return matching_fields_dict


def get_final_fields_dict(
        dict_of_potential_matches: Dict[int, List[str]]) -> Dict[int, str]:
    final_dict = {}
    while len(final_dict) < len(dict_of_potential_matches):
        for index in dict_of_potential_matches:
            if len(dict_of_potential_matches[index]) == 1:
                final_dict[index] = dict_of_potential_matches[index][0]
            else:
                for known_field in final_dict.values():
                    try:
                        dict_of_potential_matches[index].remove(known_field)
                    except ValueError:
                        pass
    return final_dict


def discard_invalid_tickets(tickets: List[List[int]],
                            rules: Dict[str, List[int]]) -> List[List[int]]:
    valid_tickets = []
    for ticket in tickets:
        if get_invalid_value(ticket, rules) is None:
            valid_tickets.append(ticket)
    return valid_tickets


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
    return None


if __name__ == "__main__":
    print("Part 1: ", part_1("input_file.txt"))
    print("Part 2: ", part_2("input_file.txt"))
