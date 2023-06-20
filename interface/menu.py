import os
import time
from interface.board_drawer import Board_drawer
from interface.colors import bcolors

class Menu:
    good_board_size_answers = ['a', 'b', 'c']
    good_diff_answers = ["a", "b", "c"]
    board_drawer = None

    def __init__(self):
        self.board_drawer = Board_drawer()


    def welcome_message(self, previous_failed_try):
        os.system('clear')
        print("TIC-TAC-TO")
        if previous_failed_try:
            print("Wrong input!")
        return input("Wanna start? (Y/N) ")


    def get_start_answer(self):
        start = self.welcome_message(False)
        while start.lower() != "y" and start.lower() != "n":
            os.system('clear')
            start = self.welcome_message(True)
        return start.lower()


    def ask_game_board_size(self, previous_failed_try):
        if previous_failed_try:
            print("Wrong input!")
        print("How many rows and columns do you want?")
        print("a: 3x3, b: 5x5, c:7x7 ")
        return input("Which one would you choose? (a, b, c) ")


    def check_game_board_size_answer(self, game_board_size_answer):
        next_size_answer = game_board_size_answer
        while next_size_answer.lower() not in self.good_board_size_answers:
            os.system('clear')
            next_size_answer = self.ask_game_board_size(True)
        return next_size_answer


    def get_game_board_size_answer(self):
        game_board_size_answer = self.ask_game_board_size(False)
        return self.check_game_board_size_answer(game_board_size_answer)


    def ask_to_make_a_step(self, previous_failed_try, already_taken):
        if previous_failed_try:
            print("Wrong input!")
        elif already_taken:
            print("Already taken!")
        return input("Make a step (Like a1/b2/c3): ")


    def check_step_answer(self, step_answer, needed_part_of_alphabet, board_record):
        next_step_answer = step_answer
        not_in_board = next_step_answer.lower() not in board_record.keys()

        if not not_in_board:
            already_taken_answer = board_record[next_step_answer] != "."
        else:
            already_taken_answer = False
            
        while not_in_board or already_taken_answer:
            os.system('clear')
            self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
            next_step_answer = self.ask_to_make_a_step(not_in_board, already_taken_answer)
            not_in_board = next_step_answer.lower() not in board_record.keys()
            
            if not not_in_board:
                already_taken_answer = board_record[next_step_answer] != "."
            
        return next_step_answer


    def get_next_step_answer(self, needed_part_of_alphabet, board_record):
        os.system('clear')
        self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
        step_answer = self.ask_to_make_a_step(False, False)
        return self.check_step_answer(step_answer, needed_part_of_alphabet, board_record)


    def robot_makes_a_move(self, needed_part_of_alphabet, board_record):
        os.system('clear')
        self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
        print("Robot turn...")
        time.sleep(1)


    def finish_game(self, who_won, needed_part_of_alphabet, board_record):
        os.system('clear')
        self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
        result = bcolors.HEADER + "Tie!" + bcolors.ENDC if who_won is None else (bcolors.OKGREEN + "User won!" + bcolors.ENDC if who_won == "X" else bcolors.FAIL + "Robot won!" + bcolors.ENDC)
        print("Finished game! " + result)


    def ask_difficulty_level(self, previous_failed_try):
        if previous_failed_try:
            print("Wrong input!")
        print("Difficulty levels: ")
        print("a, Super easy")
        print("b, Medium")
        print("c, Impossible")
        return input("Choose one (a/b/c): ")


    def check_difficulty_level_answer(self, difficulty_answer):
        diff_answer = difficulty_answer

        while diff_answer not in self.good_diff_answers:
            os.system('clear')
            diff_answer = self.ask_difficulty_level(True)
        return diff_answer


    def get_difficulty_level(self):
        os.system('clear')
        difficulty_level = self.ask_difficulty_level(False)
        return self.check_difficulty_level_answer(difficulty_level)
