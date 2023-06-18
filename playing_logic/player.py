from interface.menu import get_next_step_answer


player_value = "X"


def player_move(needed_part_of_alphabet, board_record):
    user_answer = get_next_step_answer(needed_part_of_alphabet, board_record)
    board_record[user_answer] = player_value