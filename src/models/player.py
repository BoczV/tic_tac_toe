from interface.menu import Menu
from abc import ABC, abstractmethod


class Player(ABC):
    player_value: str
    player_name: str
    menu: Menu = None
    needed_part_of_alphabet: list

    def __init__(
        self,
        player_value: str,
        player_name: str,
        menu: Menu,
        needed_part_of_alphabet: list,
    ):
        self.player_value = player_value
        self.player_name = player_name
        self.menu = menu
        self.needed_part_of_alphabet = needed_part_of_alphabet

    @abstractmethod
    def move(self, board_record: dict) -> None:
        pass
