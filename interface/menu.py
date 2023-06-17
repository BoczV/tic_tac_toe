import os
from interface.board_drawer import draw_board 


good_board_size_answers = ['a', 'b', 'c']


def welcome_message(previous_failed_try):
    print("TIC-TAC-TO")
    if previous_failed_try:
        print("Wrong input!")
    return input("Wanna start? (Y/N) ")


def get_start_answer():
    start = welcome_message(False)
    while start.lower() != "y" and start.lower() != "n":
        os.system('clear')
        start = welcome_message(True)
    return start.lower()


def ask_game_board_size(previous_failed_try):
    if previous_failed_try:
        print("Wrong input!")
    print("How many rows and columns do you want?")
    print("a: 3x3, b: 5x5, c:7x7 ")
    return input("Which one would you choose? (a, b, c) ")


def check_game_board_size_answer(game_board_size_answer):
    next_answer = game_board_size_answer
    while next_answer.lower() not in good_board_size_answers:
        os.system('clear')
        next_answer = ask_game_board_size(True)
    return next_answer


def get_game_board_size_answer():
    game_board_size_answer = ask_game_board_size(False)
    return check_game_board_size_answer(game_board_size_answer)


def start_game():
    start_answer = get_start_answer()
    os.system('clear')
    if start_answer == "y":
        board_size = get_game_board_size_answer()
        draw_board(board_size)
    else:
        print("Okay, bye!")
