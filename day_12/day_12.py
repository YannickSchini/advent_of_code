class Ship:
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


if __name__ == "__main__":
    test_ship = Ship("input_file.txt")
    print(test_ship.make_all_moves())
    print(test_ship.calculate_distance())
