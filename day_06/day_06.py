def part_1(file_path):
    with open(file_path, "r") as customs_file:
        unprocessed_customs_string = customs_file.read()
    unprocessed_customs_list = unprocessed_customs_string.split('\n\n')
    return sum(
        [len(set(x.replace('\n', ''))) for x in unprocessed_customs_list])


def part_2(file_path):
    with open(file_path, "r") as customs_file:
        unprocessed_customs_string = customs_file.read()
    unprocessed_customs_list = unprocessed_customs_string.split('\n\n')
    intermediate_list = [x.split('\n') for x in unprocessed_customs_list]
    intermediate_list_2 = [[set(y) for y in x if y != '']
                           for x in intermediate_list]
    intermediate_list_3 = [
        len(set.intersection(*x)) for x in intermediate_list_2
    ]
    print(intermediate_list_3)
    return sum(intermediate_list_3)


if __name__ == "__main__":
    print(part_1('input_file.txt'))
    print(part_2('input_file.txt'))
