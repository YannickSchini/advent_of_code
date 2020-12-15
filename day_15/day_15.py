def day_15_test(starting_number_list, number_to_go_to):
    number_list = starting_number_list
    while len(number_list) < number_to_go_to:
        if len(number_list) % 100000 == 0:
            print(starting_number_list)
        try:
            index = number_list[:-1][::-1].index(number_list[-1])
            number_list.append(index + 1)
        except ValueError:
            number_list.append(0)
    return number_list[-1]


if __name__ == "__main__":
    input_list = [1, 2, 16, 19, 18, 0]
    print("Part 1: ", day_15_test(input_list, 2020))
    print("Part 2: ", day_15_test(input_list, 30000000))
