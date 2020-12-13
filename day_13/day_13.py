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


def part_2(file_path):
    with open(file_path, "r") as bus_times_file:
        bus_times_file.readline()
        bus_ID_string = bus_times_file.readline()
    bus_ID_list = bus_ID_string.rstrip('\n').split(',')

    timestamp = 0
    continue_loop = True
    while continue_loop:
        if timestamp % 100000 == 0:
            print(timestamp)
        timestamp += min([int(x) for x in bus_ID_list if x != "x"])
        counter = 0
        for ID in bus_ID_list:
            if does_bus_run_at_timestamp(ID, timestamp + counter):
                counter += 1
                continue
            else:
                break
        if counter == len(bus_ID_list):
            continue_loop = False
    return timestamp


def does_bus_run_at_timestamp(ID, timestamp):
    if ID == 'x':
        return True
    else:
        return (timestamp % int(ID) == 0)


if __name__ == "__main__":
    print(part_1("input_file.txt"))
    print(part_2("input_file.txt"))
