def part_1(file_path):
    with open(file_path, "r") as customs_file:
        unprocessed_customs_string = customs_file.read()
    unprocessed_customs_list = unprocessed_customs_string.split('\n\n')
    return sum(
        [len(set(x.replace('\n', ''))) for x in unprocessed_customs_list])


if __name__ == "__main__":
    print(part_1('input_file.txt'))
