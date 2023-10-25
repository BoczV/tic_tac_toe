import os
import string
import platform
import secrets

from interface.menu import Menu
from models.robot import Robot
from models.human import Human
from models.player import Player
from logic.win_inspector import WinInspector

first_names: list = ["Kinga", "Réka", "Bence", "Balázs", "Viktor"]
last_names: list = ["Kiss", "Varga", "Lengyel", "Nagy"]


class Game:
    __board_size_switcher: dict = {"a": 3, "b": 5, "c": 7}
    __alphabet: list = list(string.ascii_lowercase)
    __board_record: dict
    __needed_part_of_alphabet: list
    __win_inspector: WinInspector = None
    __first_player: Player = None
    __second_player: Player = None
    __menu: Menu = None
    __size: int = 0
    __op_system: str
    __game_mode: str

    def __init__(self):
        self.__op_system = platform.system()
        self.__menu = Menu(self.__op_system)

    def setup(self) -> None:
        self.__game_mode = self.__menu.get_game_mode_answer()
        board_size_char = self.__menu.get_game_board_size_answer()
        self.__size = self.__board_size_switcher[board_size_char]
        self.init_board_record()
        self.setup_players()
        self.__win_inspector = WinInspector(
            self.__needed_part_of_alphabet,
            self.__size,
            {
                "first": self.__first_player.player_value,
                "second": self.__second_player.player_value,
            },
        )

    def setup_players(self) -> None:
        if self.__game_mode == "a":
            player_characters = ["X", "O"]
            first_player_char = secrets.choice(player_characters)
            second_player_char = "O" if first_player_char == "X" else "X"
            first_robot_name = f"{self.generate_robot_name()} (Robot1)"
            second_robot_name = f"{self.generate_robot_name()} (Robot2)"
            difficulty_level1 = self.__menu.get_difficulty_level(first_robot_name)
            difficulty_level2 = self.__menu.get_difficulty_level(second_robot_name)
            self.__first_player = Robot(
                first_player_char,
                first_robot_name,
                difficulty_level1,
                self.__needed_part_of_alphabet,
                self.__menu,
                "robot",
            )
            self.__second_player = Robot(
                second_player_char,
                second_robot_name,
                difficulty_level2,
                self.__needed_part_of_alphabet,
                self.__menu,
                "robot",
            )
        elif self.__game_mode == "b":
            user_name = self.__menu.ask_user_name_answer("User")
            user_char = self.__menu.get_character_answer(user_name).upper()
            robot_name = f"{self.generate_robot_name()} (Robot)"
            difficulty_level = self.__menu.get_difficulty_level(robot_name)
            robot_char = "O" if user_char == "X" else "X"
            self.__first_player = Human(
                user_char, user_name, self.__menu, self.__needed_part_of_alphabet
            )
            self.__second_player = Robot(
                robot_char,
                robot_name,
                difficulty_level,
                self.__needed_part_of_alphabet,
                self.__menu,
                "human",
            )
        else:
            user1_name = self.__menu.ask_user_name_answer("User1")
            user2_name = self.__menu.ask_user_name_answer("User2")
            user_char = self.__menu.get_character_answer(user1_name).upper()
            another_char = "O" if user_char == "X" else "X"
            self.__first_player = Human(
                user_char, user1_name, self.__menu, self.__needed_part_of_alphabet
            )
            self.__second_player = Human(
                another_char, user2_name, self.__menu, self.__needed_part_of_alphabet
            )

    def generate_robot_name(self) -> str:
        return secrets.choice(first_names) + " " + secrets.choice(last_names)

    def play(self) -> None:
        player_value = self.__first_player.player_value
        someone_won = False
        who_won = None
        while "." in self.__board_record.values() and not someone_won:
            self.play_one_round(player_value)
            player_value = "O" if player_value == "X" else "X"
            who_won = self.__win_inspector.check_if_someone_wins(self.__board_record)
            someone_won = who_won is not None
        sub_who_won = (
            self.__first_player.player_name
            if who_won == self.__first_player.player_value
            else self.__second_player.player_name
        )
        self.__menu.finish_game(
            who_won if who_won is None else sub_who_won,
            self.__needed_part_of_alphabet,
            self.__board_record,
        )

    def play_one_round(self, player_value: str) -> None:
        if player_value == self.__first_player.player_value:
            self.__first_player.move(self.__board_record)
        else:
            self.__second_player.move(self.__board_record)

    def init_board_record(self) -> None:
        self.__board_record = {}
        self.__needed_part_of_alphabet = []
        for i in range(self.__size):
            letter = self.__alphabet[i]
            for j in range(1, self.__size + 1):
                key = f"{letter}{j}"
                self.__board_record[key] = "."
            self.__needed_part_of_alphabet.append(letter)

    def start_game(self) -> None:
        start_answer = self.__menu.get_start_answer()
        os.system("clear" if self.__op_system != "Windows" else "cls")
        if start_answer == "y":
            self.setup()
            self.play()
            restart_answer = self.__menu.get_new_game_answer()
            if restart_answer == "y":
                self.start_game()
            else:
                print("Okay, bye!")
        else:
            print("Okay, bye!")
