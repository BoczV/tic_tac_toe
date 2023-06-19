import os
import time
from interface.board_drawer import draw_board
from interface.colors import bcolors


good_board_size_answers = ['a', 'b', 'c']
good_diff_answers = ["a", "b", "c"]


def welcome_message(previous_failed_try):
    os.system('clear')
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
    next_size_answer = game_board_size_answer
    while next_size_answer.lower() not in good_board_size_answers:
        os.system('clear')
        next_size_answer = ask_game_board_size(True)
    return next_size_answer


def get_game_board_size_answer():
    game_board_size_answer = ask_game_board_size(False)
    return check_game_board_size_answer(game_board_size_answer)


def ask_to_make_a_step(previous_failed_try, already_taken):
    if previous_failed_try:
        print("Wrong input!")
    elif already_taken:
        print("Already taken!")
    return input("Make a step (Like a1/b2/c3): ")


def check_step_answer(step_answer, needed_part_of_alphabet, board_record):
    next_step_answer = step_answer
    not_in_board = next_step_answer.lower() not in board_record.keys()

    if not not_in_board:
        already_taken_answer = board_record[next_step_answer] != "."
    else:
        already_taken_answer = False
        
    while not_in_board or already_taken_answer:
        os.system('clear')
        draw_board(needed_part_of_alphabet, board_record)
        next_step_answer = ask_to_make_a_step(not_in_board, already_taken_answer)
        not_in_board = next_step_answer.lower() not in board_record.keys()
        
        if not not_in_board:
            already_taken_answer = board_record[next_step_answer] != "."
        
    return next_step_answer


def get_next_step_answer(needed_part_of_alphabet, board_record):
    os.system('clear')
    draw_board(needed_part_of_alphabet, board_record)
    step_answer = ask_to_make_a_step(False, False)
    return check_step_answer(step_answer, needed_part_of_alphabet, board_record)


def robot_makes_a_move(needed_part_of_alphabet, board_record):
    os.system('clear')
    draw_board(needed_part_of_alphabet, board_record)
    print("Robot turn...")
    time.sleep(1)


def finish_game(who_won, needed_part_of_alphabet, board_record):
    os.system('clear')
    draw_board(needed_part_of_alphabet, board_record)
    result = bcolors.HEADER + "Tie!" + bcolors.ENDC if who_won is None else (bcolors.OKGREEN + "User won!" + bcolors.ENDC if who_won == "X" else bcolors.FAIL + "Robot won!" + bcolors.ENDC)
    print("Finished game! " + result)


def ask_difficulty_level(previous_failed_try):
    if previous_failed_try:
        print("Wrong input!")
    print("Difficulty levels: ")
    print("a, Super easy")
    print("b, Medium")
    print("c, Impossible")
    return input("Choose one (a/b/c): ")


def check_difficulty_level_answer(difficulty_answer):
    diff_answer = difficulty_answer

    while diff_answer not in good_diff_answers:
        os.system('clear')
        diff_answer = ask_difficulty_level(True)
    return diff_answer


def get_difficulty_level():
    os.system('clear')
    difficulty_level = ask_difficulty_level(False)
    return check_difficulty_level_answer(difficulty_level)
