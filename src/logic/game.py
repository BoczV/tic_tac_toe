import os
import string
import platform

from interface.menu import Menu
from logic.robot import Robot
from logic.player import Player
from logic.win_inspector import Win_inspector

class Game:
    board_size_switcher: dict = {"a": 3, "b": 5, "c": 7}
    alphabet: list = list(string.ascii_lowercase)
    board_record: dict = None
    needed_part_of_alphabet: list = None
    win_inspector: Win_inspector = None
    player: Player = None
    robot: Robot = None
    menu: Menu = None
    size: int = 0
    difficulty_level: str = None
    user_char: str = None
    op_system: str = None

    def __init__(self):
        self.op_system = platform.system()
        self.menu = Menu(self.op_system)


    def setup(self) -> None:
        board_size_char = self.menu.get_game_board_size_answer()
        self.size = self.board_size_switcher[board_size_char]
        self.user_char = self.menu.get_character_answer().upper()
        self.init_board_record()
        robot_char = "O" if self.user_char == "X" else "X"
        self.player = Player(self.user_char, self.menu, self.needed_part_of_alphabet)
        self.robot = Robot(robot_char, self.needed_part_of_alphabet, self.size, self.menu)
        self.win_inspector = Win_inspector(self.needed_part_of_alphabet, self.size, {"user": self.user_char, "robot": robot_char})


    def play(self) -> None:
        player_value = self.user_char
        someone_won = False
        who_won = None
        while "." in self.board_record.values() and not someone_won:
            self.play_one_round(player_value)
            player_value = "O" if player_value == "X" else "X"
            who_won = self.win_inspector.check_if_someone_wins(self.board_record)
            someone_won = who_won is not None
        self.menu.finish_game(None if who_won is None else ("user" if who_won == self.user_char else "robot"), self.needed_part_of_alphabet, self.board_record)


    def play_one_round(self, player_value: str) -> None:
        if player_value == self.user_char:
            self.player.player_move(self.board_record)
        else:
            self.robot_round()


    def robot_round(self) -> None:
        if self.difficulty_level == "a":
                self.robot.robot_move_easy_level(self.board_record)
        elif self.difficulty_level == "b":
            self.robot.robot_move_medium_level(self.board_record, None)
        else:
            self.robot.robot_move_impossible_level(self.board_record)


    def init_board_record(self) -> None:
        self.board_record = {}
        self.needed_part_of_alphabet = []
        for i in range(self.size):
            letter = self.alphabet[i]
            for j in range(1, self.size + 1):
                key = f"{letter}{j}"
                self.board_record[key] = "."
            self.needed_part_of_alphabet.append(letter)


    def start_game(self) -> None:
        start_answer = self.menu.get_start_answer()
        os.system('clear' if self.op_system != "Windows" else 'cls')
        if start_answer == "y":
            self.setup()
            self.difficulty_level = self.menu.get_difficulty_level()
            self.play()
            restart_answer = self.menu.get_new_game_answer()
            if restart_answer == "y":
                self.start_game()
            else:
                print("Okay, bye!")
        else:
            print("Okay, bye!")