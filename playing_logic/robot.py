import random
from interface.menu import robot_makes_a_move


player_value = "O"
possible_winning_options = []


def setup_informations_for_robot(size, needed_part_of_alphabet):
    for i in range(1, size + 1):
        possible_winning_option = []
        for j in range(len(needed_part_of_alphabet)):
            possible_winning_option.append(f"{needed_part_of_alphabet[j]}{i}")
        possible_winning_options.append(possible_winning_option)
    
    for j in range(len(needed_part_of_alphabet)):
        possible_winning_option = []
        for i in range(1, size + 1):
            possible_winning_option.append(f"{needed_part_of_alphabet[j]}{i}")
        possible_winning_options.append(possible_winning_option)

    possible_winning_option1 = []
    possible_winning_option2 = []
    for k in range(len(needed_part_of_alphabet)):
        possible_winning_option1.append(f"{needed_part_of_alphabet[k]}{k + 1}")
        possible_winning_option2.append(f"{needed_part_of_alphabet[len(needed_part_of_alphabet) - 1 - k] + str(k + 1)}")

    possible_winning_options.append(possible_winning_option1)
    possible_winning_options.append(possible_winning_option2)


def robot_move_easy_level(needed_part_of_alphabet, board_record):
    available_places = find_available_places(board_record)
    robot_makes_a_move(needed_part_of_alphabet, board_record)
    random_key = random.choice(available_places)
    board_record[random_key] = player_value


def robot_move_medium_level(board_record, needed_part_of_alphabet):
    robot_makes_a_move(needed_part_of_alphabet, board_record)
    available_places = find_available_places(board_record)
    possible_blocking_option_for_danger = find_a_dangerous_path_to_block(board_record, len(needed_part_of_alphabet))

    if possible_blocking_option_for_danger != []:
        random_key = random.choice([element for element in possible_blocking_option_for_danger if element in available_places])
        board_record[random_key] = player_value
    else:
        possible_promising_winning_option = find_a_promising_path_to_move(board_record, len(needed_part_of_alphabet))
        if possible_promising_winning_option != []:
            random_key = random.choice([element for element in possible_promising_winning_option if element in available_places])
            board_record[random_key] = player_value
        else:
            possible_winning_option = find_a_good_path_to_move(board_record, len(needed_part_of_alphabet))
            if possible_winning_option != []:
                random_key = random.choice([element for element in possible_winning_option if element in available_places])
                board_record[random_key] = player_value
            else:
                possible_path_to_block = find_a_possible_path_to_block(board_record, len(needed_part_of_alphabet))
                if possible_path_to_block != []:
                    random_key = random.choice([element for element in possible_path_to_block if element in available_places])
                    board_record[random_key] = player_value
                else:
                    robot_move_easy_level(needed_part_of_alphabet, board_record)


def find_available_places(board_record):
    result = []
    for i, j in board_record.items():
        if j == ".":
            result.append(i)
    return result


def find_a_good_path_to_move(board_record, board_size):
    return find_a_path(board_record, board_size, "O")


def find_a_possible_path_to_block(board_record, board_size):
    return find_a_path(board_record, board_size, "X")


def find_a_path(board_record, board_size, player_value):
    for possible_winning_option in possible_winning_options:
        counter = 0
        for j in possible_winning_option:
            element = board_record[j]
            if element == "." or element == player_value:
                counter += 1
        if counter == board_size:
            return possible_winning_option
    return []


def find_a_dangerous_path_to_block(board_record, board_size):
    return find_a_serious_path(board_record, board_size, "X")


def find_a_promising_path_to_move(board_record, board_size):
    return find_a_serious_path(board_record, board_size, "O")


def find_a_serious_path(board_record, board_size, player_value):
    for possible_winning_option in possible_winning_options:
        counter = 0
        user_counter = 0
        for j in possible_winning_option:
            element = board_record[j]
            if element == "." or element == player_value:
                counter += 1
            if element == player_value:
                user_counter += 1
        if counter == board_size and (user_counter >= board_size - 2 if board_size > 3 else user_counter > board_size - 2):
            return possible_winning_option
    return []