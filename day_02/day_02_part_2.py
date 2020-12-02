def load_file(path):
    with open (path, "r") as myfile:
        list_of_lines = myfile.readlines()
        list_of_lines = [x.strip() for x in list_of_lines]
    return list_of_lines

def parse_entry(entry):
    entry_list = entry.split(":")
    password = entry_list[1].lstrip(' ')
    partially_parsed_policy = entry_list[0].split(" ")
    policy = ((int(partially_parsed_policy[0].split("-")[0]), int(partially_parsed_policy[0].split("-")[1])), partially_parsed_policy[1])
    return policy, password

def check_if_passport_is_valid(policy, password):
    acceptable_positions, letter = policy
    first_position, second_position = acceptable_positions
    if (password[first_position - 1] == letter) ^ (password[second_position - 1] == letter):
        return True
    else:
        return False


def day_02_resolution(password_and_policy_filepath):
    password_and_policy_list = load_file(password_and_policy_filepath)
    counter = 0
    for entry in password_and_policy_list:
        policy, password = parse_entry(entry)
        if check_if_passport_is_valid(policy, password):
            counter = counter + 1
    print(counter)

if __name__ == "__main__":
    day_02_resolution("password_and_policy_file.txt")
