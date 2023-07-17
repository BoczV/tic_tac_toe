import os
import string
import platform
import random

from interface.menu import Menu
from models.robot import Robot
from models.human import Human
from models.player import Player
from logic.win_inspector import Win_inspector

class Game:
    board_size_switcher: dict = {"a": 3, "b": 5, "c": 7}
    alphabet: list = list(string.ascii_lowercase)
    board_record: dict = None
    needed_part_of_alphabet: list = None
    win_inspector: Win_inspector = None
    first_player: Player = None
    second_player: Player = None
    menu: Menu = None
    size: int = 0
    op_system: str = None
    game_mode: str = None
    first_names: list = ["Kinga", "Réka", "Bence", "Balázs", "Viktor"]
    last_names: list = ["Kiss", "Varga", "Lengyel", "Nagy"]

    def __init__(self):
        self.op_system = platform.system()
        self.menu = Menu(self.op_system)


    def setup(self) -> None:
        self.game_mode = self.menu.get_game_mode_answer()
        board_size_char = self.menu.get_game_board_size_answer()
        self.size = self.board_size_switcher[board_size_char]
        self.init_board_record()
        difficulty_level = self.menu.get_difficulty_level() if self.game_mode != "c" else None
        self.setup_players(difficulty_level)
        self.win_inspector = Win_inspector(self.needed_part_of_alphabet, self.size, {"first": self.first_player.player_value, "second": self.second_player.player_value})


    def setup_players(self, difficulty_level: str) -> None:
        if self.game_mode == "a":
            player_characters = ['X', 'O']
            first_player_char = random.choice(player_characters)
            second_player_char = "O" if first_player_char == "X" else "X"
            first_robot_name = f"{self.generate_robot_name()} (Robot1)"
            second_robot_name = f"{self.generate_robot_name()} (Robot2)"
            self.first_player = Robot(first_player_char, first_robot_name, difficulty_level, self.needed_part_of_alphabet, self.menu, "robot")
            self.second_player = Robot(second_player_char, second_robot_name, difficulty_level, self.needed_part_of_alphabet, self.menu, "robot")
        elif self.game_mode == "b":
            user_name = self.menu.ask_user_name_answer("User")
            user_char = self.menu.get_character_answer(user_name).upper()
            robot_name = f"{self.generate_robot_name()} (Robot)"
            robot_char = "O" if user_char == "X" else "X"
            self.first_player = Human(user_char, user_name, self.menu, self.needed_part_of_alphabet)
            self.second_player = Robot(robot_char, robot_name, difficulty_level, self.needed_part_of_alphabet, self.menu, "human")
        else:
            user1_name = self.menu.ask_user_name_answer("User1")
            user2_name = self.menu.ask_user_name_answer("User2")
            user_char = self.menu.get_character_answer(user1_name).upper()
            another_char = "O" if user_char == "X" else "X"
            self.first_player = Human(user_char, user1_name, self.menu, self.needed_part_of_alphabet)
            self.second_player = Human(another_char, user2_name, self.menu, self.needed_part_of_alphabet)


    def generate_robot_name(self) -> str:
        return random.choice(self.first_names)+" "+random.choice(self.last_names)

    def play(self) -> None:
        player_value = self.first_player.player_value
        someone_won = False
        who_won = None
        while "." in self.board_record.values() and not someone_won:
            self.play_one_round(player_value)
            player_value = "O" if player_value == "X" else "X"
            who_won = self.win_inspector.check_if_someone_wins(self.board_record)
            someone_won = who_won is not None
        self.menu.finish_game(None if who_won is None else (self.first_player.player_name if who_won == self.first_player.player_value else self.second_player.player_name), self.needed_part_of_alphabet, self.board_record)


    def play_one_round(self, player_value: str) -> None:
        if player_value == self.first_player.player_value:
            self.first_player.move(self.board_record)
        else:
            self.second_player.move(self.board_record)


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
            self.play()
            restart_answer = self.menu.get_new_game_answer()
            if restart_answer == "y":
                self.start_game()
            else:
                print("Okay, bye!")
        else:
            print("Okay, bye!")