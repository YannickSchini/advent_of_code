import re


def part_1(file_path):
    with open(file_path, "r") as input_file:
        docking_program = input_file.readlines()
    docking_program = [x.rstrip("\n") for x in docking_program]
    memory = {}
    for line in docking_program:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            key, numerical_value = re.match("^mem\[(\d+)\] = (\d+)$",
                                            line).groups(0)
            memory[key] = apply_mask_part_1(int(numerical_value), mask)
    return sum(memory.values())


def apply_mask_part_1(value, mask):
    binary_value = format(value, "0" + str(len(mask)) + 'b')
    binary_result = "".join([
        binary_value[index] if mask[index] == 'X' else mask[index]
        for index in range(len(binary_value))
    ])
    return int(binary_result, 2)


def part_2(file_path):
    with open(file_path, "r") as input_file:
        docking_program = input_file.readlines()
    docking_program = [x.rstrip("\n") for x in docking_program]
    memory = {}
    for line in docking_program:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            address, numerical_value = re.match("^mem\[(\d+)\] = (\d+)$",
                                                line).groups(0)
            for key in apply_mask_part_2(address, mask):
                memory[key] = int(numerical_value)
    return sum(memory.values())


def apply_mask_part_2(address, mask):
    binary_address = format(int(address), "0" + str(len(mask)) + "b")
    result = ''
    for index in range(len(mask)):
        if mask[index] == "0":
            result += binary_address[index]
        elif mask[index] == "1":
            result += "1"
        elif mask[index] == "X":
            result += "X"
        else:
            raise ValueError
    possible_addresses = replace_one_X(result)
    return flatten(possible_addresses)


def replace_one_X(input_string):
    if "X" not in input_string:
        return input_string
    else:
        return [
            replace_one_X(input_string.replace("X", "0", 1)),
            replace_one_X(input_string.replace("X", "1", 1))
        ]


def flatten(possiblyNestedList):
    if not isinstance(possiblyNestedList, list):
        return
    flattened = []
    for item in possiblyNestedList:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened


if __name__ == "__main__":
    print(part_1("input_file.txt"))
    print(part_2("input_file.txt"))
