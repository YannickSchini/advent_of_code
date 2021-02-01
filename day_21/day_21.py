from typing import Dict, Tuple, List
from collections import Counter


def part_1(file_path: str) -> int:
    food_dict = parse_inputs(file_path)
    allergens_dict = get_dict_of_possible_ingredients_for_each_allergen(
        food_dict)
    return allergens_dict


def parse_inputs(file_path: str) -> Dict[str, Tuple[List[str], List[str]]]:
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
    food_dict = {}
    for i in range(len(lines)):
        food_dict["Food " + str(i)] = get_list_of_ingredients_and_allergens(
            lines[i])
    return food_dict


def get_list_of_ingredients_and_allergens(
        food: str) -> Tuple[List[str], List[str]]:
    food = food.rstrip("\n")
    ingredients, allergens = food.split(" (")
    ingredients = [x.rstrip(",") for x in ingredients.split(" ")]
    allergens = [x.rstrip(")") for x in allergens.split(" ")[1:]]
    allergens = [x.rstrip(",") for x in allergens]
    return ingredients, allergens


def get_dict_of_possible_ingredients_for_each_allergen(
        food_dict: Dict[str, Tuple[List[str],
                                   List[str]]]) -> Dict[str, List[str]]:
    allergens_dict = {}
    for food in food_dict:
        ingredients, allergens = food_dict[food]
        for allergen in allergens:
            if allergen in allergens_dict:
                allergens_dict[allergen] += ingredients
            else:
                allergens_dict[allergen] = ingredients.copy()
    for allergen in allergens_dict:
        allergens_dict[allergen] = Counter(allergens_dict[allergen])
    return allergens_dict


def refine_dict_of_allergens(
        allergens_dict: Dict[str, List[str]]) -> Dict[str, List[str]]:
    while len(allergens_dict) < sum(
                            [len(allergens_dict[x]) for x in allergens_dict]):
        print("Test")


if __name__ == "__main__":
    # print(part_1("input_file.txt"))
    print(part_1("test_file.txt"))
