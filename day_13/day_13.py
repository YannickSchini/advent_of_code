import operator


def part_1(file_path):
    with open(file_path, "r") as bus_times_file:
        lines = bus_times_file.readlines()
    departure_time = int(lines[0].rstrip('\n'))
    bus_IDs_string = lines[1]
    bus_IDs_list = bus_IDs_string.rstrip('\n').split(',')
    bus_times = {}
    for ID in bus_IDs_list:
        if ID == "x":
            pass
        else:
            bus_times[int(ID)] = (departure_time // int(ID) + 1) * int(ID)
    best_bus_ID = min(bus_times.items(), key=operator.itemgetter(1))[0]
    return best_bus_ID * (bus_times[best_bus_ID] - departure_time)


if __name__ == "__main__":
    print(part_1("input_file.txt"))
