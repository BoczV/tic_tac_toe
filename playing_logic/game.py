import os
import string
import random

from interface.menu import get_game_board_size_answer, get_start_answer, get_next_step_answer, finish_game, robot_makes_a_move


board_size_swithcer = {"a": 3, "b": 5, "c": 7}
alphabet = list(string.ascii_lowercase)
board_record = {}
needed_part_of_alphabet = []


def start_game():
    board_size_char = get_game_board_size_answer()
    board_size = board_size_swithcer[board_size_char]
    init_board_record(board_size)
    return board_size


def play(size):
    player_value = "X"
    someone_won = False
    who_won = None
    while "." in board_record.values() and not someone_won:
        play_one_round(player_value)
        player_value = "O" if player_value == "X" else "X"
        who_won = check_if_someone_wins(size)
        someone_won = who_won is not None
    finish_game(who_won, needed_part_of_alphabet, board_record)


def play_one_round(player_value):
    if player_value == "X":
        player_move(player_value)
    else:
        robot_move(player_value)


def player_move(player_value):
    user_answer = get_next_step_answer(needed_part_of_alphabet, board_record)
    board_record[user_answer] = player_value


def robot_move(player_value):
    robot_makes_a_move(needed_part_of_alphabet, board_record)
    random_key = random.choice(list(board_record.keys()))
    while board_record[random_key] != ".":
        random_key = random.choice(list(board_record.keys()))
    board_record[random_key] = player_value


def check_if_robot_wins(size):
    player_value = "O"
    if check_if_someone_wins_horizontally(player_value, size):
        return True
    elif check_if_someone_wins_vertically(player_value, size):
        return True
    elif check_if_someone_wins_cross_diagonally(player_value, size):
        return True
    return False


def check_if_human_wins(size):
    player_value = "X"
    if check_if_someone_wins_horizontally(player_value, size):
        return True
    elif check_if_someone_wins_vertically(player_value, size):
        return True
    elif check_if_someone_wins_cross_diagonally(player_value, size):
        return True
    return False


def check_if_someone_wins(size):
    result = None
    if check_if_human_wins(size):
        result = "X"
    elif check_if_robot_wins(size):
        result = "O"
    return result


def check_if_someone_wins_vertically(player_value, size):
    counter = 0
    for i in needed_part_of_alphabet:
        for j in range(1, len(needed_part_of_alphabet) + 1):
            key = f"{i}{j}"
            if board_record[key] == player_value:
                counter += 1
        if counter == size:
            return True
        else:
            counter = 0
    return False


def check_if_someone_wins_horizontally(player_value, size):
    counter = 0
    for j in range(1, len(needed_part_of_alphabet) + 1):
        for i in needed_part_of_alphabet:
            key = f"{i}{j}"
            if board_record[key] == player_value:
                counter += 1
        if counter == size:
            return True
        else:
            counter = 0
    return False


def check_if_someone_wins_cross_diagonally(player_value, size):
    counter = 0
    for i in range(len(needed_part_of_alphabet)):
        key = f"{needed_part_of_alphabet[i] + str(i + 1)}"
        if board_record[key] == player_value:
            counter += 1
    if counter == size:
            return True
    else:
        counter = 0

    for j in range(len(needed_part_of_alphabet)):
        key = f"{needed_part_of_alphabet[len(needed_part_of_alphabet) - 1 - j] + str(j + 1)}"
        if board_record[key] == player_value:
            counter += 1
    if counter == size:
            return True
    else:
        counter = 0


def init_board_record(size):
    for i in range(size):
        letter = alphabet[i]
        for j in range(1, size + 1):
            key = f"{letter}{j}"
            board_record[key] = "."
        needed_part_of_alphabet.append(letter)


def game():
    start_answer = get_start_answer()
    os.system('clear')
    if start_answer == "y":
        board_size = start_game()
        play(board_size)
    else:
        print("Okay, bye!")