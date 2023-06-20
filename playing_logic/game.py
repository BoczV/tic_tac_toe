import os
import string

from interface.menu import get_game_board_size_answer, get_start_answer, finish_game, get_difficulty_level
from playing_logic.robot import robot_move_easy_level, setup_informations_for_robot, robot_move_medium_level, robot_move_impossible_level
from playing_logic.player import player_move
from playing_logic.win_inspector import Win_inspector

class Game:
    board_size_swithcer = {"a": 3, "b": 5, "c": 7}
    alphabet = list(string.ascii_lowercase)
    board_record = {}
    needed_part_of_alphabet = []
    win_inspector = None


    def __init__(self):
        self.win_inspector = Win_inspector() 


    def start_game(self):
        board_size_char = get_game_board_size_answer()
        board_size = self.board_size_swithcer[board_size_char]
        self.init_board_record(board_size)
        setup_informations_for_robot(board_size, self.needed_part_of_alphabet)
        return board_size


    def play(self, size, difficulty_level):
        player_value = "X"
        someone_won = False
        who_won = None
        while "." in self.board_record.values() and not someone_won:
            self.play_one_round(player_value, difficulty_level)
            player_value = "O" if player_value == "X" else "X"
            who_won = self.win_inspector.check_if_someone_wins(size, self.needed_part_of_alphabet, self.board_record)
            someone_won = who_won is not None
        finish_game(who_won, self.needed_part_of_alphabet, self.board_record)


    def play_one_round(self, player_value, difficulty_level):
        if player_value == "X":
            player_move(self.needed_part_of_alphabet, self.board_record)
        else:
            self.robot_round(difficulty_level)


    def robot_round(self, difficulty_level):
        if difficulty_level == "a":
                robot_move_easy_level(self.needed_part_of_alphabet, self.board_record)
        elif difficulty_level == "b":
            robot_move_medium_level(self.board_record, self.needed_part_of_alphabet)
        else:
            robot_move_impossible_level(self.board_record, self.needed_part_of_alphabet)


    def init_board_record(self, size):
        for i in range(size):
            letter = self.alphabet[i]
            for j in range(1, size + 1):
                key = f"{letter}{j}"
                self.board_record[key] = "."
            self.needed_part_of_alphabet.append(letter)


    def game(self):
        start_answer = get_start_answer()
        os.system('clear')
        if start_answer == "y":
            board_size = self.start_game()
            difficulty_level = get_difficulty_level()
            self.play(board_size, difficulty_level)
        else:
            print("Okay, bye!")