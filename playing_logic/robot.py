import random


class Robot:
    player_value = None
    opponent_value = None
    possible_winning_options = None
    corners = None
    needed_part_of_alphabet = None
    menu = None
    size = 0
    user_wants_to_continue_answer = None

    def __init__(self, player_value, needed_part_of_alphabet, size, menu):
        self.player_value = player_value
        self.opponent_value = "X" if player_value == "O" else "O"
        self.menu = menu
        self.needed_part_of_alphabet = needed_part_of_alphabet
        self.size = size
        self.setup_information_for_robot()


    def setup_information_for_robot(self):
        self.possible_winning_options = []
        for i in range(1, self.size + 1):
            possible_winning_option = []
            for j in range(self.size):
                possible_winning_option.append(f"{self.needed_part_of_alphabet[j]}{i}")
            self.possible_winning_options.append(possible_winning_option)
        
        for j in range(self.size):
            possible_winning_option = []
            for i in range(1, self.size + 1):
                possible_winning_option.append(f"{self.needed_part_of_alphabet[j]}{i}")
            self.possible_winning_options.append(possible_winning_option)

        possible_winning_option1 = []
        possible_winning_option2 = []
        for k in range(self.size):
            possible_winning_option1.append(f"{self.needed_part_of_alphabet[k]}{k + 1}")
            possible_winning_option2.append(f"{self.needed_part_of_alphabet[self.size - 1 - k] + str(k + 1)}")

        self.possible_winning_options.append(possible_winning_option1)
        self.possible_winning_options.append(possible_winning_option2)
        self.setup_corners()


    def setup_corners(self):
        self.corners = []
        self.corners.append(f"{self.needed_part_of_alphabet[0]}{1}")
        self.corners.append(f"{self.needed_part_of_alphabet[self.size - 1]}{1}")
        self.corners.append(f"{self.needed_part_of_alphabet[0]}{self.size}")
        self.corners.append(f"{self.needed_part_of_alphabet[self.size - 1]}{self.size}")


    def robot_move_easy_level(self, board_record):
        available_places = self.find_available_places(board_record)
        self.menu.robot_makes_a_move(self.needed_part_of_alphabet, board_record)
        random_key = random.choice(available_places)
        board_record[random_key] = self.player_value


    def robot_move_medium_level(self, board_record, received_available_places):
        self.menu.robot_makes_a_move(self.needed_part_of_alphabet, board_record)
        available_places = self.find_available_places(board_record) if received_available_places is None else received_available_places
        possible_blocking_option_for_danger = self.find_a_dangerous_path_to_block(board_record)

        if possible_blocking_option_for_danger != []:
            random_key = random.choice([element for element in possible_blocking_option_for_danger if element in available_places])
            board_record[random_key] = self.player_value
        else:
            possible_promising_winning_option = self.find_a_promising_path_to_move(board_record)
            if possible_promising_winning_option != []:
                random_key = random.choice([element for element in possible_promising_winning_option if element in available_places])
                board_record[random_key] = self.player_value
            else:
                possible_winning_option = self.find_a_good_path_to_move(board_record)
                if possible_winning_option != []:
                    random_key = random.choice([element for element in possible_winning_option if element in available_places])
                    board_record[random_key] = self.player_value
                else:
                    possible_path_to_block = self.find_a_possible_path_to_block(board_record)
                    if possible_path_to_block != []:
                        random_key = random.choice([element for element in possible_path_to_block if element in available_places])
                        board_record[random_key] = self.player_value
                    else:
                        if self.user_wants_to_continue_answer is None:
                            self.user_wants_to_continue_answer = self.menu.get_continue_answer()
                            if self.user_wants_to_continue_answer == "y":
                                self.robot_move_easy_level(board_record)
                            else:
                                self.menu.exit_program()
                        else:
                            self.robot_move_easy_level(board_record)


    def robot_move_impossible_level(self, board_record):
        self.menu.robot_makes_a_move(self.needed_part_of_alphabet, board_record)
        available_places = self.find_available_places(board_record)
        if len(available_places) == self.size * self.size - 1:
            half = self.size // 2 + 1
            key = f"{self.needed_part_of_alphabet[half - 1]}{half}"
            if key in available_places:
                board_record[key] = self.player_value
            else:
                self.find_available_places_in_corner(available_places, board_record)
        else:
            self.robot_move_medium_level(board_record, available_places)


    def find_available_places_in_corner(self, available_places, board_record):
        for element in available_places:
            if element in self.corners:
                board_record[element] = self.player_value
                break


    def find_available_places(self, board_record):
        result = []
        for i, j in board_record.items():
            if j == ".":
                result.append(i)
        return result


    def find_a_good_path_to_move(self, board_record):
        return self.find_a_path(board_record, self.player_value)


    def find_a_possible_path_to_block(self, board_record):
        return self.find_a_path(board_record, self.opponent_value)


    def find_a_path(self, board_record, player_value):
        for possible_winning_option in self.possible_winning_options:
            counter = 0
            for j in possible_winning_option:
                element = board_record[j]
                if element == "." or element == player_value:
                    counter += 1
            if counter == self.size:
                return possible_winning_option
        return []


    def find_a_dangerous_path_to_block(self, board_record):
        return self.find_a_serious_path(board_record, self.opponent_value)


    def find_a_promising_path_to_move(self, board_record):
        return self.find_a_serious_path(board_record, self.player_value)


    def find_a_serious_path(self, board_record, player_value):
        for possible_winning_option in self.possible_winning_options:
            counter = 0
            user_counter = 0
            for j in possible_winning_option:
                element = board_record[j]
                if element == "." or element == player_value:
                    counter += 1
                if element == player_value:
                    user_counter += 1
            if counter == self.size and (user_counter >= self.size - 2 if self.size > 3 else user_counter > self.size - 2):
                return possible_winning_option
        return []