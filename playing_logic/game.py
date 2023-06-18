import os
import string
import random
from interface.board_drawer import draw_board
from interface.menu import get_game_board_size_answer, get_start_answer, get_next_step_answer 


board_size_swithcer = {"a": 3, "b": 5, "c": 7}
alphabet = list(string.ascii_lowercase)
board_record = {}
needed_part_of_alphabet = []


def start_game():
    board_size = get_game_board_size_answer()
    size = board_size_swithcer[board_size]
    init_board_record(size)


def play():
    player_value = "X"
    while "." in board_record.values():
        play_one_round(player_value)
        player_value = "O" if player_value == "X" else "X"

    finish_game()


def play_one_round(player_value):
    if player_value == "X":
        player_move(player_value)
    else:
        robot_move(player_value)


def player_move(player_value):
    os.system('clear')
    draw_board(needed_part_of_alphabet, board_record)
    user_answer = get_next_step_answer(needed_part_of_alphabet, board_record)
    board_record[user_answer] = player_value


def robot_move(player_value):
    random_key = random.choice(list(board_record.keys()))
    while board_record[random_key] != ".":
        random_key = random.choice(list(board_record.keys()))
    board_record[random_key] = player_value


def finish_game():
    os.system('clear')
    draw_board(needed_part_of_alphabet, board_record)
    print("Finished game!")


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
        start_game()
        play()
    else:
        print("Okay, bye!")