from typing import Tuple


def part_1(file_path: str) -> int:
    with open(file_path, "r") as input_file:
        tile_string_list = input_file.readlines()
    tile_dict = {}
    for tile_str in tile_string_list:
        tile_coord = get_coord_from_str(tile_str)
        if tile_coord in tile_dict:
            tile_dict[tile_coord] = not tile_dict[tile_coord]
        else:
            tile_dict[tile_coord] = True
    return sum(tile_dict.values())


def get_coord_from_str(tile_string: str) -> Tuple[float, int]:
    ne_count = tile_string.count("ne")
    se_count = tile_string.count("se")
    nw_count = tile_string.count("nw")
    sw_count = tile_string.count("sw")
    e_count = tile_string.count("e") - ne_count - se_count
    w_count = tile_string.count("w") - nw_count - sw_count
    return (e_count + 0.5 * ne_count + 0.5 * se_count - w_count -
            0.5 * nw_count - 0.5 * sw_count,
            ne_count + nw_count - se_count - sw_count)


if __name__ == "__main__":
    print(part_1("input_file.txt"))
