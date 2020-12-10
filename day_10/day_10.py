from typing import List


def part_1(list_of_adapters: List[int]) -> int:
    #  Outlet value
    list_of_adapters.append(0)
    #  Built-in adapter
    list_of_adapters.append(max(list_of_adapters) + 3)
    list_of_adapters.sort()
    list_of_differences = [
        list_of_adapters[i + 1] - list_of_adapters[i]
        for i in range(len(list_of_adapters) - 1)
    ]
    if max(list_of_differences) > 3:
        print("Houston, we have a problem")
    return list_of_differences.count(1) * list_of_differences.count(3)


def part_2(list_of_adapters: List[int]) -> int:
    """
    Function taken from https://github.com/MariaMokbel/advent-of-code-2020
    as I wasn't able to figure out how to tackle this problem
    """
    list_of_adapters.sort()
    possibilities = {0: 1}
    for adapter in list_of_adapters:
        possibilities[adapter] = 0
        if adapter - 1 in possibilities:
            possibilities[adapter] += possibilities[adapter - 1]

        if adapter - 2 in possibilities:
            possibilities[adapter] += possibilities[adapter - 2]

        if adapter - 3 in possibilities:
            possibilities[adapter] += possibilities[adapter - 3]
    return possibilities[max(list_of_adapters)]


if __name__ == "__main__":
    with open("input_file.txt", "r") as input_file:
        list_of_adapters = input_file.readlines()
    list_of_adapters = [int(x) for x in list_of_adapters]
    print("Part 1: ", part_1(list_of_adapters.copy()))
    print("Part 2: ", part_2(list_of_adapters.copy()))
