def process_instruction(instruction):
    if instruction[:3] == "nop":
        return (0, 1)
    elif instruction[:3] == "jmp":
        return (0, int(instruction[4:]))
    elif instruction[:3] == "acc":
        return (int(instruction[4:]), 1)
    else:
        return ValueError


def process_boot_code(instruction_list):
    accumulator = 0
    index = 0
    already_visited_indexes = [0]
    while True:
        try:
            accumulator_increment, index_increment = process_instruction(
                instruction_list[index])
        except IndexError:
            return (1, accumulator)
        accumulator += accumulator_increment
        index += index_increment
        if index in already_visited_indexes:
            break
        else:
            already_visited_indexes.append(index)
    return (0, accumulator)


def check_if_boot_program_is_fixed(instruction_list):
    exit_status, accumulator = process_boot_code(instruction_list)
    return exit_status


def fix_bootloader(instruction_list):
    for index in range(len(instruction_list)):
        if instruction_list[index][:3] == "acc":
            pass
        elif instruction_list[index][:3] == "jmp":
            potentially_fixed_instruction_list = instruction_list.copy()
            potentially_fixed_instruction_list[
                index] = "nop" + potentially_fixed_instruction_list[index][3:]
            if check_if_boot_program_is_fixed(
                    potentially_fixed_instruction_list):
                return process_boot_code(potentially_fixed_instruction_list)
        elif instruction_list[index][:3] == "nop":
            potentially_fixed_instruction_list = instruction_list.copy()
            potentially_fixed_instruction_list[
                index] = "jmp" + potentially_fixed_instruction_list[index][3:]
            if check_if_boot_program_is_fixed(
                    potentially_fixed_instruction_list):
                return process_boot_code(potentially_fixed_instruction_list)
        else:
            raise ValueError


if __name__ == "__main__":
    with open("input_file.txt", "r") as boot_loader_code:
        instruction_list = boot_loader_code.readlines()
    print("Part 1:", process_boot_code(instruction_list))
    print("Part 2:", fix_bootloader(instruction_list))
