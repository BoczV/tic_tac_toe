import os
import string

from interface.menu import Menu
from playing_logic.robot import Robot
from playing_logic.player import Player
from playing_logic.win_inspector import Win_inspector

class Game:
    board_size_swithcer = {"a": 3, "b": 5, "c": 7}
    alphabet = list(string.ascii_lowercase)
    board_record = {}
    needed_part_of_alphabet = []
    win_inspector = None
    player = None
    robot = None
    menu = None
    size = 0
    difficulty_level = None

    def __init__(self):
        self.player = Player("X")
        self.menu = Menu()


    def start_game(self):
        board_size_char = self.menu.get_game_board_size_answer()
        self.size = self.board_size_swithcer[board_size_char]
        self.init_board_record()
        self.robot.setup_informations_for_robot()


    def play(self):
        player_value = "X"
        someone_won = False
        who_won = None
        while "." in self.board_record.values() and not someone_won:
            self.play_one_round(player_value)
            player_value = "O" if player_value == "X" else "X"
            who_won = self.win_inspector.check_if_someone_wins(self.board_record)
            someone_won = who_won is not None
        self.menu.finish_game(who_won, self.needed_part_of_alphabet, self.board_record)


    def play_one_round(self, player_value):
        if player_value == "X":
            self.player.player_move(self.needed_part_of_alphabet, self.board_record)
        else:
            self.robot_round()


    def robot_round(self):
        if self.difficulty_level == "a":
                self.robot.robot_move_easy_level(self.board_record)
        elif self.difficulty_level == "b":
            self.robot.robot_move_medium_level(self.board_record, None)
        else:
            self.robot.robot_move_impossible_level(self.board_record)


    def init_board_record(self):
        for i in range(self.size):
            letter = self.alphabet[i]
            for j in range(1, self.size + 1):
                key = f"{letter}{j}"
                self.board_record[key] = "."
            self.needed_part_of_alphabet.append(letter)
        self.robot = Robot("O", self.needed_part_of_alphabet, self.size)
        self.win_inspector = Win_inspector(self.needed_part_of_alphabet, self.size)


    def game(self):
        start_answer = self.menu.get_start_answer()
        os.system('clear')
        if start_answer == "y":
            self.start_game()
            self.difficulty_level = self.menu.get_difficulty_level()
            self.play()
        else:
            print("Okay, bye!")