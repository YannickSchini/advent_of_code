from typing import Tuple, List


def parse_inputs(file_path: str) -> Tuple[List[int], List[int]]:
    with open(file_path, "r") as input_file:
        input_string = input_file.read()
    player_1_deck, player_2_deck = input_string.split("\n\n")
    player_1_deck = [
        int(x) for x in player_1_deck.split("\n") if x[:6] != "Player"
    ]
    player_2_deck = [
        int(x) for x in player_2_deck.split("\n")[:-1] if x[:6] != "Player"
    ]
    return player_1_deck, player_2_deck


def part_1(file_path: str) -> int:
    player_1_deck, player_2_deck = parse_inputs(file_path)
    number_of_turns, winning_deck = play_one_game(player_1_deck, player_2_deck)
    return calculate_score(winning_deck)


def play_one_turn(player_1_deck: List[int],
                  player_2_deck: List[int]) -> Tuple[List[int], List[int]]:
    new_player_1_deck = player_1_deck.copy()
    new_player_2_deck = player_2_deck.copy()
    player_1_card = new_player_1_deck.pop(0)
    player_2_card = new_player_2_deck.pop(0)
    if player_1_card > player_2_card:
        new_player_1_deck.extend([player_1_card, player_2_card])
        return new_player_1_deck, new_player_2_deck
    else:
        new_player_2_deck.extend([player_2_card, player_1_card])
        return new_player_1_deck, new_player_2_deck


def play_one_game(player_1_deck: List[int],
                  player_2_deck: List[int]) -> Tuple[int, List[int]]:
    turn_counter = 0
    while len(player_1_deck) > 0 and len(player_2_deck) > 0:
        player_1_deck, player_2_deck = play_one_turn(player_1_deck,
                                                     player_2_deck)
        turn_counter += 1
    return turn_counter, player_1_deck + player_2_deck


def calculate_score(player_deck: List[int]) -> int:
    score = 0
    for index in range(len(player_deck)):
        score += (index + 1) * player_deck[len(player_deck) - 1 - index]
    return score


if __name__ == "__main__":
    print(part_1("input_file.txt"))
