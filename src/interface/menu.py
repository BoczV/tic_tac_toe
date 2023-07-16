import os
import sys
import time
from interface.board_drawer import Board_drawer
from interface.colors import Colors

class Menu:
    good_board_size_answers: list = ['a', 'b', 'c']
    good_diff_answers: list = ["a", "b", "c"]
    board_drawer: Board_drawer = None
    os_command: str = None

    def __init__(self, op_system: str):
        self.os_command = 'clear' if op_system != "Windows" else 'cls'
        self.board_drawer = Board_drawer()


    def welcome_message(self, previous_failed_try: bool) -> str:
        os.system(self.os_command)
        print("TIC-TAC-TO")
        if previous_failed_try:
            print("Wrong input!")
        return input("Wanna start? (Y/N) ")


    def get_start_answer(self) -> str:
        start = self.welcome_message(False)
        while start.lower() != "y" and start.lower() != "n":
            os.system(self.os_command)
            start = self.welcome_message(True)
        return start.lower()


    def ask_game_board_size(self, previous_failed_try: bool) -> str:
        os.system(self.os_command)
        if previous_failed_try:
            print("Wrong input!")
        print("How many rows and columns do you want?")
        print("a: 3x3, b: 5x5, c:7x7 ")
        return input("Which one would you choose? (a, b, c) ")


    def check_game_board_size_answer(self, game_board_size_answer: str) -> str:
        next_size_answer = game_board_size_answer
        while next_size_answer.lower() not in self.good_board_size_answers:
            os.system(self.os_command)
            next_size_answer = self.ask_game_board_size(True)
        return next_size_answer


    def get_game_board_size_answer(self) -> str:
        game_board_size_answer = self.ask_game_board_size(False)
        return self.check_game_board_size_answer(game_board_size_answer)


    def ask_to_make_a_step(self, previous_failed_try: bool, already_taken: bool) -> str:
        if previous_failed_try:
            print("Wrong input!")
        elif already_taken:
            print("Already taken!")
        return input("Make a step (Like a1/b2/c3): ")


    def check_step_answer(self, step_answer: str, needed_part_of_alphabet: list, board_record: dict) -> str:
        next_step_answer = step_answer
        not_in_board = next_step_answer.lower() not in board_record.keys()
        if not not_in_board:
            already_taken_answer = board_record[next_step_answer] != "."
        else:
            already_taken_answer = False
        while not_in_board or already_taken_answer:
            os.system(self.os_command)
            self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
            next_step_answer = self.ask_to_make_a_step(not_in_board, already_taken_answer)
            not_in_board = next_step_answer.lower() not in board_record.keys()
            
            if not not_in_board:
                already_taken_answer = board_record[next_step_answer] != "."
        return next_step_answer


    def get_next_step_answer(self, user_name: str, needed_part_of_alphabet: list, board_record: dict) -> str:
        os.system(self.os_command)
        self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
        print(f"{user_name}'s turn")
        step_answer = self.ask_to_make_a_step(False, False)
        return self.check_step_answer(step_answer, needed_part_of_alphabet, board_record)


    def robot_makes_a_move(self, robot_name: str, needed_part_of_alphabet: list, board_record: dict) -> None:
        os.system(self.os_command)
        self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
        print(f"{robot_name}'s turn...")
        time.sleep(1)


    def finish_game(self, who_won: str, needed_part_of_alphabet: list, board_record: dict) -> None:
        os.system(self.os_command)
        self.board_drawer.draw_board(needed_part_of_alphabet, board_record)
        result = Colors.HEADER + "Tie!" + Colors.END if who_won is None else Colors.GREEN + f"{who_won} won!" + Colors.END
        print("Finished game! " + result)


    def ask_difficulty_level(self, previous_failed_try: bool) -> str:
        if previous_failed_try:
            print("Wrong input!")
        print("Difficulty levels: ")
        print("a, Super easy")
        print("b, Medium")
        print("c, Impossible")
        return input("Choose one (a/b/c): ")


    def check_difficulty_level_answer(self, difficulty_answer: str) -> str:
        diff_answer = difficulty_answer
        while diff_answer not in self.good_diff_answers:
            os.system(self.os_command)
            diff_answer = self.ask_difficulty_level(True)
        return diff_answer


    def get_difficulty_level(self) -> str:
        os.system(self.os_command)
        difficulty_level = self.ask_difficulty_level(False)
        return self.check_difficulty_level_answer(difficulty_level)
    

    def ask_continue_answer(self, previous_failed_try: bool) -> str:
        if previous_failed_try:
            print("Wrong input!")
        print("Robot: It's pointless to continue, none of us could win.")
        return input("Would you like to continue? (Y/N) ")


    def check_continue_answer(self, continue_answer: str) -> str:
        con_answer = continue_answer
        while con_answer != "y" and con_answer != "n":
            os.system(self.os_command)
            con_answer = self.ask_continue_answer(True).lower()
        return con_answer


    def get_continue_answer(self) -> str:
        os.system(self.os_command)
        continue_answer = self.ask_continue_answer(False).lower()
        return self.check_continue_answer(continue_answer)


    def exit_program(self) -> None:
        print("Ok, bye!")
        sys.exit()
    

    def ask_character_answer(self, previous_failed_try: bool, user_name: str) -> str:
        if previous_failed_try:
            print("Wrong input!")
        return input(f"Which character do you choose, {user_name}? (X/O) ")


    def check_character_answer(self, user_name: str, character_answer: str) -> str:
        char_answer = character_answer
        while char_answer.lower() != "x" and char_answer.lower() != "o":
            os.system(self.os_command)
            char_answer = self.ask_character_answer(True, user_name)
        return char_answer


    def get_character_answer(self, user_name: str) -> str:
        os.system(self.os_command)
        char_answer = self.ask_character_answer(False, user_name)
        return self.check_character_answer(user_name, char_answer)
    

    def ask_new_game_answer(self, previous_failed_try: bool) -> str:
        if previous_failed_try:
            print("Wrong input!")
        return input("Start again? (Y/N) ")


    def check_new_game_answer(self, new_game_answer: str) -> str:
        n_game_answer = new_game_answer.lower()
        while n_game_answer != "y" and n_game_answer != "n":
            os.system(self.os_command)
            n_game_answer = self.ask_new_game_answer(True).lower()
        return n_game_answer


    def get_new_game_answer(self) -> str:
        new_game_answer = self.ask_new_game_answer(False)
        return self.check_new_game_answer(new_game_answer)
    

    def ask_game_mode_answer(self, previous_failed_try: bool) -> str:
        if previous_failed_try:
            print("Wrong input!")
        print("Game modes: ")
        print("a, Robot vs Robot")
        print("b, Human vs Robot")
        print("c, Human vs Human")
        return input("Which mode do you choose? (a/b/c) ")


    def check_game_mode_answer(self, game_mode_answer: str) -> str:
        g_mode_answer = game_mode_answer.lower()
        while g_mode_answer not in self.good_diff_answers:
            os.system(self.os_command)
            g_mode_answer = self.ask_game_mode_answer(True).lower()
        return g_mode_answer


    def get_game_mode_answer(self) -> str:
        os.system(self.os_command)
        game_mode_answer = self.ask_game_mode_answer(False)
        return self.check_game_mode_answer(game_mode_answer)


    def ask_user_name_answer(self, user_string: str) -> str:
        os.system(self.os_command)
        return input(f"Tell us your name, {user_string}: ")