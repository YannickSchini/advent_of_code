import re


def part_1(file_path: str):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
    counter = 0
    for line in lines:
        while "(" in line:
            line = replace_first_inner_parenthesis(line)
            print(line)
        counter += evaluate_expression_without_parenthesis(line)
    return counter


def evaluate_expression_without_parenthesis(expresion: str) -> int:
    elements = expresion.split(' ')
    counter = int(elements.pop(0))
    while len(elements) > 0:
        element = elements.pop(0)
        if element in ("+", "*"):
            counter = perform_operation(counter, int(elements.pop(0)), element)
        else:
            print(elements)
    return counter


def perform_operation(number_1: int, number_2: int, operation: str) -> int:
    if operation == "+":
        return number_1 + number_2
    elif operation == "*":
        return number_1 * number_2
    else:
        raise ValueError


def replace_first_inner_parenthesis(expresion: str) -> str:
    match = re.search("\(\d+( [+|*] \d+)+\)", expresion)
    if match:
        return expresion.replace(
            match.group(),
            str(evaluate_expression_without_parenthesis(match.group(0)[1:-1])),
            1)
    else:
        return expresion


if __name__ == "__main__":
    print(part_1("input_file.txt"))
