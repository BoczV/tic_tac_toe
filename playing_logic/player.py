from interface.menu import Menu


class Player:
    player_value = None
    menu = None

    def __init__(self, player_value):
        self.player_value = player_value
        self.menu = Menu()


    def player_move(self, needed_part_of_alphabet, board_record):
        user_answer = self.menu.get_next_step_answer(needed_part_of_alphabet, board_record)
        board_record[user_answer] = self.player_value