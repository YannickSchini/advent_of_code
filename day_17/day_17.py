from typing import Dict, List, Tuple

neighbor_list_3D = [(-1, -1, -1), (-1, 0, -1), (0, -1, -1), (0, 0, -1),
                    (1, 0, -1), (0, 1, -1),
                    (1, 1, -1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1),
                    (-1, 0, 1), (0, -1, 1), (0, 0, 1), (1, 0, 1), (0, 1, 1),
                    (1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, 0), (-1, 0, 0),
                    (0, -1, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (1, -1, 0),
                    (-1, 1, 0)]

neighbor_list_4D = []
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                neighbor_list_4D.append((i, j, k, l))
neighbor_list_4D.remove((0, 0, 0, 0))


def part_1(file_path: str):
    starting_topology = parse_inputs(file_path)
    topo_1 = get_new_topology_3D(starting_topology)
    topo_2 = get_new_topology_3D(topo_1)
    topo_3 = get_new_topology_3D(topo_2)
    topo_4 = get_new_topology_3D(topo_3)
    topo_5 = get_new_topology_3D(topo_4)
    topo_6 = get_new_topology_3D(topo_5)
    return list(topo_6.values()).count("#")


def part_2(file_path: str):
    starting_topology = parse_inputs(file_path)
    topo_1 = get_new_topology_4D(starting_topology)
    topo_2 = get_new_topology_4D(topo_1)
    topo_3 = get_new_topology_4D(topo_2)
    topo_4 = get_new_topology_4D(topo_3)
    topo_5 = get_new_topology_4D(topo_4)
    topo_6 = get_new_topology_4D(topo_5)
    return list(topo_6.values()).count("#")


def parse_inputs(file_path: str) -> Dict[Tuple[int], str]:
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
    starting_topology = {}
    for line_num in range(len(lines)):
        for col_num in range(len(lines[0])):
            starting_topology[(line_num, col_num, 0,
                               0)] = lines[line_num][col_num]
    return starting_topology


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


def get_new_topology_4D(
        topology: Dict[Tuple[int], str]) -> Dict[Tuple[int], str]:
    new_topology = topology.copy()
    for cube in topology:
        for neighbor in neighbor_list_4D:
            if tuple(map(sum, zip(cube, neighbor))) in topology.keys():
                pass
            else:
                new_topology[tuple(map(sum, zip(
                    cube, neighbor)))] = update_status_of_cube(
                        ".",
                        get_number_of_active_neighbors_4D(
                            tuple(map(sum, zip(cube, neighbor))), topology))
        new_topology[cube] = update_status_of_cube(
            topology[cube], get_number_of_active_neighbors_4D(cube, topology))
    return new_topology


def update_status_of_cube(status: str, number_of_active_neighbors: int) -> str:
    if status == "#" and number_of_active_neighbors in (2, 3):
        return "#"
    elif status == "#" and number_of_active_neighbors not in (2, 3):
        return "."
    elif status == "." and number_of_active_neighbors == 3:
        return "#"
    else:
        return "."


def get_number_of_active_neighbors_3D(coordinates: Tuple[int],
                                      topology: Dict[Tuple[int], str]) -> int:
    x, y, z, w = coordinates
    counter = 0
    for neighbor in neighbor_list_3D:
        delta_x, delta_y, delta_z, delta_w = neighbor + (0, )
        try:
            if topology[(x + delta_x, y + delta_y, z + delta_z,
                         w + delta_w)] == "#":
                counter += 1
            else:
                pass
        except KeyError:
            pass
    return counter


def get_number_of_active_neighbors_4D(coordinates: Tuple[int],
                                      topology: Dict[Tuple[int], str]) -> int:
    x, y, z, w = coordinates
    counter = 0
    for neighbor in neighbor_list_4D:
        delta_x, delta_y, delta_z, delta_w = neighbor
        try:
            if topology[(x + delta_x, y + delta_y, z + delta_z,
                         w + delta_w)] == "#":
                counter += 1
            else:
                pass
        except KeyError:
            pass
    return counter


if __name__ == "__main__":
    file_path = "input_file.txt"
    print(part_1(file_path))
    print(part_2(file_path))
