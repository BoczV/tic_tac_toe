class Player:
    player_value = None
    menu = None
    needed_part_of_alphabet = None

    def __init__(self, player_value, menu, needed_part_of_alphabet):
        self.player_value = player_value
        self.menu = menu
        self.needed_part_of_alphabet = needed_part_of_alphabet


    def player_move(self, board_record):
        user_answer = self.menu.get_next_step_answer(self.needed_part_of_alphabet, board_record)
        board_record[user_answer] = self.player_value