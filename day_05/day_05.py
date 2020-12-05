def get_row(boarding_pass: str) -> int:
    return get_numerical_from_text('F', 'B', boarding_pass[:7])


def get_column(boarding_pass: str) -> int:
    return get_numerical_from_text('L', 'R', boarding_pass[7:])


def get_numerical_from_text(symbol_for_low: str, symbol_for_high: str,
                            input_string: str) -> int:
    return int(
        input_string.replace(symbol_for_high,
                             '1').replace(symbol_for_low, '0'), 2)


def get_id(boarding_pass: str):
    row = get_row(boarding_pass)
    column = get_column(boarding_pass)
    return row * 8 + column


if __name__ == "__main__":
    with open('input_file.txt', "r") as boarding_pass_file:
        boarding_pass_list = boarding_pass_file.readlines()
    id_list = []
    for boarding_pass in boarding_pass_list:
        id_list.append(get_id(boarding_pass))

    # print(id_list)
    print("First part:", max(id_list))
    print("Second part:", [
        x for x in range(0, 955)
        if x not in id_list and x + 1 in id_list and x - 1 in id_list
    ])
