class Ship_part_1:
    def __init__(self, file_path):
        self.coord = (0, 0)
        self.direction = 90
        self.instructions = self._load_instructions(file_path)

    @staticmethod
    def _load_instructions(file_path):
        with open(file_path, "r") as instruction_file:
            list_of_instruction_strings = instruction_file.readlines()
            list_of_instruction_strings = [
                x.rstrip('\n') for x in list_of_instruction_strings
            ]
            instructions = []
            for instruction_string in list_of_instruction_strings:
                instructions.append(
                    (instruction_string[0], int(instruction_string[1:])))
            return instructions

    def _make_one_move(self, instruction):
        command, value = instruction
        x_coord, y_coord = self.coord
        if command == "N" or (command == "F" and self.direction == 0):
            self.coord = (x_coord, y_coord + value)
        elif command == "S" or (command == "F" and self.direction == 180):
            self.coord = (x_coord, y_coord - value)
        elif command == "E" or (command == "F" and self.direction == 90):
            self.coord = (x_coord - value, y_coord)
        elif command == "W" or (command == "F" and self.direction == 270):
            self.coord = (x_coord + value, y_coord)
        elif command == "L":
            self.direction = (self.direction - value) % 360
        elif command == "R":
            self.direction = (self.direction + value) % 360
        else:
            raise ValueError

    def make_all_moves(self):
        for instruction in self.instructions:
            self._make_one_move(instruction)
        return self.coord

    def calculate_distance(self):
        x_coord, y_coord = self.coord
        return abs(x_coord) + abs(y_coord)


class Ship_part_2:
    def __init__(self, file_path):
        self.coord = (0, 0)
        self.waypoint_direction = (-10, 1)
        self.instructions = self._load_instructions(file_path)

    @staticmethod
    def _load_instructions(file_path):
        with open(file_path, "r") as instruction_file:
            list_of_instruction_strings = instruction_file.readlines()
            list_of_instruction_strings = [
                x.rstrip('\n') for x in list_of_instruction_strings
            ]
            instructions = []
            for instruction_string in list_of_instruction_strings:
                instructions.append(
                    (instruction_string[0], int(instruction_string[1:])))
            return instructions

    def _make_one_move(self, instruction):
        print(instruction)
        command, value = instruction
        x_coord, y_coord = self.coord
        x_direction, y_direction = self.waypoint_direction
        if command == "F":
            self.coord = (x_coord + value * x_direction,
                          y_coord + value * y_direction)
            x_coord, y_coord = self.coord
        elif command == "N":
            self.waypoint_direction = (x_direction, y_direction + value)
        elif command == "S":
            self.waypoint_direction = (x_direction, y_direction - value)
        elif command == "E":
            self.waypoint_direction = (x_direction - value, y_direction)
        elif command == "W":
            self.waypoint_direction = (x_direction + value, y_direction)
        elif command == "L":
            for i in range(value // 90):
                self.waypoint_direction = self._turn_left(
                    x_direction, y_direction)
                x_direction, y_direction = self.waypoint_direction
        elif command == "R":
            for i in range(value // 90):
                self.waypoint_direction = self._turn_right(
                    x_direction, y_direction)
                x_direction, y_direction = self.waypoint_direction
        else:
            raise ValueError
        print(self.coord, self.waypoint_direction)

    @staticmethod
    def _turn_left(x_coord, y_coord):
        return (y_coord, -1 * x_coord)

    @staticmethod
    def _turn_right(x_coord, y_coord):
        return (-1 * y_coord, x_coord)

    def _get_direction_to_waypoint(self):
        x_coord, y_coord = self.coord
        wp_x_coord, wp_y_coord = self.waypoint_direction
        return (wp_x_coord - x_coord, wp_y_coord - y_coord)

    def make_all_moves(self):
        for instruction in self.instructions:
            self._make_one_move(instruction)
        return self.coord

    def calculate_distance(self):
        x_coord, y_coord = self.coord
        return abs(x_coord) + abs(y_coord)


if __name__ == "__main__":
    ship_part_1 = Ship_part_1("input_file.txt")
    print(ship_part_1.make_all_moves())
    print(ship_part_1.calculate_distance())
    ship_part_2 = Ship_part_2("input_file.txt")
    print(ship_part_2.make_all_moves())
    print(ship_part_2.calculate_distance())
