from interface.menu import Menu
from models.player import Player


class Human(Player):
    def __init__(
        self,
        player_value: str,
        player_name: str,
        menu: Menu,
        needed_part_of_alphabet: list,
    ) -> None:
        super().__init__(player_value, player_name, menu, needed_part_of_alphabet)

    def move(self, board_record: dict) -> None:
        user_answer = self.menu.get_next_step_answer(
            self.player_name, self.needed_part_of_alphabet, board_record
        )
        board_record[user_answer] = self.player_value
