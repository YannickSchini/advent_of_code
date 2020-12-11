from typing import List


class seatingArea:
    def __init__(self, file_path):
        self.floor_plan: List[List[str]] = self._get_floor_plan_from_file(
            file_path)
        self.seats = self._get_seat_dict()
        self.adjacent_seat_combinations = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                                           (0, 1), (1, -1), (1, 0), (1, 1)]

    @staticmethod
    def _get_floor_plan_from_file(file_path):
        with open(file_path, "r") as floor_plan_file:
            return [x.strip('\n') for x in floor_plan_file.readlines()]

    def _get_seat_dict(self):
        seat_dict = {}
        for row_number in range(len(self.floor_plan)):
            for column_number in range(len(self.floor_plan[row_number])):
                seat_dict[(row_number, column_number
                           )] = self.floor_plan[row_number][column_number]
        return seat_dict

    def _get_seat_value(self, row_num, col_num):
        if row_num < 0 or col_num < 0 or row_num >= len(
                self.floor_plan) or col_num >= len(self.floor_plan[0]):
            return IndexError
        else:
            return self.seats[(row_num, col_num)]

    def update_seat_status_part_1(self, row_num, col_num):
        current_seat_status = self.seats[(row_num, col_num)]
        number_of_adjacent_occupied_seats = 0
        for row_offset, col_offset in self.adjacent_seat_combinations:
            new_seat_value = self._get_seat_value(row_num + row_offset,
                                                  col_num + col_offset)
            if new_seat_value == IndexError:
                pass
            elif new_seat_value == '#':
                number_of_adjacent_occupied_seats += 1
        if current_seat_status == "L" and number_of_adjacent_occupied_seats == 0:
            return "#"
        elif current_seat_status == "#" and number_of_adjacent_occupied_seats >= 4:
            return "L"
        else:
            return current_seat_status

    def update_seating_status(self):
        new_seat_dict = self.seats.copy()
        for row_num, col_num in self.seats.keys():
            new_seat_dict[(row_num, col_num)] = self.update_seat_status_part_2(
                row_num, col_num)
        return new_seat_dict

    def get_stabilised_occupied_seat_count(self):
        new_seat_dict = self.update_seating_status()
        while new_seat_dict != self.seats:
            self.seats = new_seat_dict
            new_seat_dict = self.update_seating_status()
        return sum([(seat_value == "#") for seat_value in self.seats.values()])

    def update_seat_status_part_2(self, row_num, col_num):
        current_seat_status = self.seats[(row_num, col_num)]
        number_of_adjacent_occupied_seats = 0
        for row_offset, col_offset in self.adjacent_seat_combinations:
            total_row_offset = row_offset
            total_col_offset = col_offset
            while self._get_seat_value(row_num + total_row_offset,
                                       col_num + total_col_offset) == '.':
                total_row_offset += row_offset
                total_col_offset += col_offset
            new_seat_value = self._get_seat_value(row_num + total_row_offset,
                                                  col_num + total_col_offset)
            if new_seat_value == IndexError:
                pass
            elif new_seat_value == '#':
                number_of_adjacent_occupied_seats += 1
        if current_seat_status == "L" and number_of_adjacent_occupied_seats == 0:
            return "#"
        elif current_seat_status == "#" and number_of_adjacent_occupied_seats >= 5:
            return "L"
        else:
            return current_seat_status


if __name__ == "__main__":
    boarding_area = seatingArea("input_file.txt")
    print("Seat number: ", boarding_area.get_stabilised_occupied_seat_count())
