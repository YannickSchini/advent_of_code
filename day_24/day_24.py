from typing import Tuple, Dict

neighbor_coords = [(-1, 0), (1, 0), (-0.5, 1), (0.5, 1), (-0.5, -1), (0.5, -1)]


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


def get_number_of_adjacent_black_tiles(
        coord: Tuple[float, int], tile_dict: Dict[Tuple[float, int],
                                                  bool]) -> int:
    counter = 0
    for neighbor in neighbor_coords:
        try:
            if tile_dict[tuple(map(sum, zip(coord, neighbor)))]:
                counter += 1
            else:
                pass
        except IndexError:
            pass
    return counterza


# SEE DAY 17 FOR INFORMATION
if __name__ == "__main__":
    print(part_1("input_file.txt"))


def get_new_topology_3D(
        topology: Dict[Tuple[int], str]) -> Dict[Tuple[int], str]:
    new_topology = topology.copy()
    for cube in topology:
        for neighbor in neighbor_list_3D:
            if tuple(map(sum, zip(cube, neighbor + (0, )))) in topology.keys():
                pass
            else:
                new_topology[tuple(map(sum, zip(
                    cube, neighbor + (0, ))))] = update_status_of_cube(
                        ".",
                        get_number_of_active_neighbors_3D(
                            tuple(map(sum, zip(cube, neighbor + (0, )))),
                            topology))
        new_topology[cube] = update_status_of_cube(
            topology[cube], get_number_of_active_neighbors_3D(cube, topology))
        return new_topology
