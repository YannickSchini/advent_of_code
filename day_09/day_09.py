def can_number_be_decomposed(number: int, number_list: list) -> bool:
    for index in range(len(number_list)):
        if (number - number_list[index]) in number_list[index + 1:]:
            return True
    return False


def process_xmas_file(number_list: list, PREAMBLE_SIZE: int) -> int:
    for index in range(PREAMBLE_SIZE, len(number_list)):
        if can_number_be_decomposed(number_list[index],
                                    number_list[index - PREAMBLE_SIZE:index]):
            pass
        else:
            return number_list[index]
    return ValueError


def find_sublist_that_sums_to_number(number: int, number_list: list) -> list:
    for index in range(len(number_list)):
        sublist_sum = number_list[index]
        sublist_len = 1
        while sublist_sum < number:
            sublist_sum += number_list[index + sublist_len]
            sublist_len += 1
        if sublist_sum == number:
            return number_list[index:index + sublist_len]
        else:
            pass
    return ValueError


if __name__ == "__main__":
    file_path = "input_file.txt"
    with open(file_path, "r") as xmas_input:
        number_list = xmas_input.readlines()
        number_list = [int(x) for x in number_list]
    number_with_property = process_xmas_file(number_list, 25)
    print("Part 1:", number_with_property)
    sublist = find_sublist_that_sums_to_number(number_with_property,
                                               number_list)
    print(sublist)
    print("Part 2:", min(sublist) + max(sublist))
