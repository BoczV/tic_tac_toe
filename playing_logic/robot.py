import random
from interface.menu import robot_makes_a_move

player_value = "O"

def robot_move(needed_part_of_alphabet, board_record):
    robot_makes_a_move(needed_part_of_alphabet, board_record)
    random_key = random.choice(list(board_record.keys()))
    while board_record[random_key] != ".":
        random_key = random.choice(list(board_record.keys()))
    board_record[random_key] = player_value