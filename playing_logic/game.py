import os
import string

from interface.menu import get_game_board_size_answer, get_start_answer, finish_game, get_difficulty_level
from playing_logic.robot import robot_move_easy_level, setup_informations_for_robot, robot_move_medium_level, robot_move_impossible_level
from playing_logic.player import player_move
from playing_logic.win_inspector import check_if_someone_wins


board_size_swithcer = {"a": 3, "b": 5, "c": 7}
alphabet = list(string.ascii_lowercase)
board_record = {}
needed_part_of_alphabet = []


def start_game():
    board_size_char = get_game_board_size_answer()
    board_size = board_size_swithcer[board_size_char]
    init_board_record(board_size)
    setup_informations_for_robot(board_size, needed_part_of_alphabet)
    return board_size


def play(size, difficulty_level):
    player_value = "X"
    someone_won = False
    who_won = None
    while "." in board_record.values() and not someone_won:
        play_one_round(player_value, difficulty_level)
        player_value = "O" if player_value == "X" else "X"
        who_won = check_if_someone_wins(size, needed_part_of_alphabet, board_record)
        someone_won = who_won is not None
    finish_game(who_won, needed_part_of_alphabet, board_record)


def play_one_round(player_value, difficulty_level):
    if player_value == "X":
        player_move(needed_part_of_alphabet, board_record)
    else:
        robot_round(difficulty_level)


def robot_round(difficulty_level):
    if difficulty_level == "a":
            robot_move_easy_level(needed_part_of_alphabet, board_record)
    elif difficulty_level == "b":
        robot_move_medium_level(board_record, needed_part_of_alphabet)
    else:
        robot_move_impossible_level(board_record, needed_part_of_alphabet)


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
        difficulty_level = get_difficulty_level()
        play(board_size, difficulty_level)
    else:
        print("Okay, bye!")