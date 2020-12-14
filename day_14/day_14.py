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
            memory[key] = apply_mask(int(numerical_value), mask)

    return sum(memory.values())


def apply_mask(value, mask):
    binary_value = format(value, "0" + str(len(mask)) + 'b')
    binary_result = "".join([
        binary_value[index] if mask[index] == 'X' else mask[index]
        for index in range(len(binary_value))
    ])
    return int(binary_result, 2)


if __name__ == "__main__":
    print(part_1("input_file.txt"))
