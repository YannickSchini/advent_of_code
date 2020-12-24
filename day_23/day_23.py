from typing import Tuple, List


def part_1(input_cup_string: str, number_of_games: int) -> str:
    cup_list = [int(x) for x in list(input_cup_string)]
    current_cup_index = 0
    current_cup = cup_list[current_cup_index]
    for game_number in range(number_of_games):
        cup_list = play_one_round(current_cup, current_cup_index, cup_list)
        current_cup_index = cup_list.index(current_cup) + 1
        current_cup_index = current_cup_index % len(cup_list)
        current_cup = cup_list[current_cup_index % len(cup_list)]
    return get_result_from_cuplist(cup_list)


def part_2(input_cup_string: str, number_of_games: int) -> str:
    cup_list = [int(x) for x in list(input_cup_string)]
    cup_list = cup_list + list(range(10, 1000001))
    current_cup_index = 0
    current_cup = cup_list[current_cup_index]
    for game_number in range(number_of_games):
        cup_list = play_one_round(current_cup, current_cup_index, cup_list)
        current_cup_index = cup_list.index(current_cup) + 1
        current_cup_index = current_cup_index % len(cup_list)
        current_cup = cup_list[current_cup_index % len(cup_list)]
    index_of_1 = cup_list.index(1)
    return cup_list[index_of_1 + 1] * cup_list[index_of_1 + 2]


def get_result_from_cuplist(cup_list: List[int]) -> str:
    index_of_1 = cup_list.index(1)
    result_list = cup_list[index_of_1 + 1:] + cup_list[:index_of_1]
    return ''.join([str(x) for x in result_list])


def play_one_round(current_cup: int, current_cup_index: int,
                   cup_list: List[int]) -> List[int]:
    removed_cups = []
    for _ in range(3):
        try:
            removed_cups.append(cup_list.pop(current_cup_index + 1))
        except IndexError:
            removed_cups.append(cup_list.pop(0))
    destination_cup_index, destination_cup = get_destination_cup(
        current_cup_index, current_cup, cup_list)
    cup_list = cup_list[:destination_cup_index + 1] + \
        removed_cups + cup_list[destination_cup_index + 1:]
    return cup_list


def get_destination_cup(current_cup_index: int, current_cup: int,
                        cup_list: List[int]) -> Tuple[int, int]:
    destination_cup = None
    while destination_cup is None:
        if current_cup == min(cup_list):
            destination_cup = max(cup_list)
        elif current_cup - 1 in cup_list:
            destination_cup = current_cup - 1
        else:
            current_cup = current_cup - 1
    destination_cup_index = cup_list.index(destination_cup)
    return destination_cup_index, destination_cup


if __name__ == "__main__":
    print(part_1("398254716", 100))
