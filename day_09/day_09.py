def can_number_be_decomposed(number: int, number_list: list) -> bool:
    for index in range(len(number_list)):
        if (number - number_list[index]) in number_list[index + 1:]:
            return True
    return False


def process_xmas_file(file_path: str, PREAMBLE_SIZE: int) -> int:
    with open(file_path, "r") as xmas_input:
        number_list = xmas_input.readlines()
        number_list = [int(x) for x in number_list]
    for index in range(PREAMBLE_SIZE, len(number_list)):
        if can_number_be_decomposed(number_list[index],
                                    number_list[index - PREAMBLE_SIZE:index]):
            pass
        else:
            return number_list[index]
    return ValueError


if __name__ == "__main__":
    print("Part 1:", process_xmas_file("input_file.txt", 25))
