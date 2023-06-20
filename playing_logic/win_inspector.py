
class Win_inspector:
    value_switcher = {"user": "X", "robot": "O"}

    def __init__(self):
        pass


    def check_if_actor_wins(self, player_value, size, needed_part_of_alphabet, board_record):
        if self.check_if_someone_wins_horizontally(player_value, size, needed_part_of_alphabet, board_record):
            return True
        elif self.check_if_someone_wins_vertically(player_value, size, needed_part_of_alphabet, board_record):
            return True
        elif self.check_if_someone_wins_cross_diagonally(player_value, size, needed_part_of_alphabet, board_record):
            return True
        return False


    def check_if_someone_wins(self, size, needed_part_of_alphabet, board_record):
        result = None
        if self.check_if_actor_wins(self.value_switcher["user"], size, needed_part_of_alphabet, board_record):
            result = self.value_switcher["user"]
        elif self.check_if_actor_wins(self.value_switcher["robot"], size, needed_part_of_alphabet, board_record):
            result = self.value_switcher["robot"]
        return result


    def check_if_someone_wins_vertically(self, player_value, size, needed_part_of_alphabet, board_record):
        counter = 0
        for i in needed_part_of_alphabet:
            for j in range(1, len(needed_part_of_alphabet) + 1):
                key = f"{i}{j}"
                if board_record[key] == player_value:
                    counter += 1
            if counter == size:
                return True
            else:
                counter = 0
        return False


    def check_if_someone_wins_horizontally(self, player_value, size, needed_part_of_alphabet, board_record):
        counter = 0
        for j in range(1, len(needed_part_of_alphabet) + 1):
            for i in needed_part_of_alphabet:
                key = f"{i}{j}"
                if board_record[key] == player_value:
                    counter += 1
            if counter == size:
                return True
            else:
                counter = 0
        return False


    def check_if_someone_wins_cross_diagonally(self, player_value, size, needed_part_of_alphabet, board_record):
        counter = 0
        for i in range(len(needed_part_of_alphabet)):
            key = f"{needed_part_of_alphabet[i] + str(i + 1)}"
            if board_record[key] == player_value:
                counter += 1
        if counter == size:
                return True
        else:
            counter = 0

        for j in range(len(needed_part_of_alphabet)):
            key = f"{needed_part_of_alphabet[len(needed_part_of_alphabet) - 1 - j] + str(j + 1)}"
            if board_record[key] == player_value:
                counter += 1
        if counter == size:
                return True
        else:
            counter = 0