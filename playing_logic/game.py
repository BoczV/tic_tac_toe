import os
import string
from interface.board_drawer import draw_board
from interface.menu import get_game_board_size_answer,get_start_answer 


board_size_swithcer = {"a": 3, "b": 5, "c": 7}
alphabet = list(string.ascii_lowercase)
board_record = {}
needed_part_of_alphabet = []


def start_game():
    start_answer = get_start_answer()
    os.system('clear')
    if start_answer == "y":
        board_size = get_game_board_size_answer()
        size = board_size_swithcer[board_size]
        init_board_record(size)
        draw_board(needed_part_of_alphabet, board_record)
    else:
        print("Okay, bye!")


def init_board_record(size):
    for i in range(size):
        letter = alphabet[i]
        for j in range(1, size + 1):
            key = f"{letter}{j}"
            board_record[key] = "."
        needed_part_of_alphabet.append(letter)