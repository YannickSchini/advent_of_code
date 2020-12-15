def part_1(starting_number_list):
    number_list = starting_number_list
    while len(number_list) < 2020:
        if number_list[-1] not in number_list[:-1]:
            number_list.append(0)
        else:
            index_list = [
                index for index in range(len(number_list) - 1)
                if number_list[index] == number_list[-1]
            ]
            number_list.append(len(number_list) - max(index_list) - 1)
    return number_list[-1]


if __name__ == "__main__":
    input_list = [1, 2, 16, 19, 18, 0]
    print(part_1(input_list))
