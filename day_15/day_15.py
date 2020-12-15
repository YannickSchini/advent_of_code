def day_15_test(starting_number_list, number_to_go_to):
    number_list = starting_number_list
    number_dict = {}
    for index, value in enumerate(starting_number_list[:-1]):
        number_dict[value] = index
    element_count = len(number_list)
    while element_count < number_to_go_to:
        try:
            number_list.append(element_count - number_dict[number_list[-1]] -
                               1)
        except KeyError:
            number_list.append(0)
        number_dict[number_list[-2]] = element_count - 1
        element_count += 1
    return number_list[-1]


if __name__ == "__main__":
    input_list = [1, 2, 16, 19, 18, 0]
    print("Part 1: ", day_15_test(input_list, 2020))
    print("Part 2: ", day_15_test(input_list, 30000000))
