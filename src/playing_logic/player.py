from interface.menu import Menu

class Player:
    player_value: str = None
    menu: Menu = None
    needed_part_of_alphabet: list = None

    def __init__(self, player_value: str, menu: Menu, needed_part_of_alphabet: list):
        self.player_value = player_value
        self.menu = menu
        self.needed_part_of_alphabet = needed_part_of_alphabet


    def player_move(self, board_record: dict):
        user_answer = self.menu.get_next_step_answer(self.needed_part_of_alphabet, board_record)
        board_record[user_answer] = self.player_value