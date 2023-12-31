class WinInspector:
    __value_switcher: dict
    __needed_part_of_alphabet: list
    __size: int = 0

    def __init__(self, needed_part_of_alphabet: list, size: int, value_switcher: dict):
        self.__needed_part_of_alphabet = needed_part_of_alphabet
        self.__size = size
        self.__value_switcher = value_switcher

    def check_if_actor_wins(self, player_value: str, board_record: dict) -> bool:
        if (
            self.check_if_someone_wins_horizontally(player_value, board_record)
            or self.check_if_someone_wins_vertically(player_value, board_record)
            or self.check_if_someone_wins_cross_diagonally(player_value, board_record)
        ):
            return True
        return False

    def check_if_someone_wins(self, board_record: dict) -> bool:
        result = None
        if self.check_if_actor_wins(self.__value_switcher["first"], board_record):
            result = self.__value_switcher["first"]
        elif self.check_if_actor_wins(self.__value_switcher["second"], board_record):
            result = self.__value_switcher["second"]
        return result

    def check_if_someone_wins_horizontally(
        self, player_value: str, board_record: dict
    ) -> bool:
        counter = 0
        for i in self.__needed_part_of_alphabet:
            for j in range(1, self.__size + 1):
                key = f"{i}{j}"
                if board_record[key] == player_value:
                    counter += 1
            if counter == self.__size:
                return True
            else:
                counter = 0
        return False

    def check_if_someone_wins_vertically(
        self, player_value: str, board_record: dict
    ) -> bool:
        counter = 0
        for j in range(1, self.__size + 1):
            for i in self.__needed_part_of_alphabet:
                key = f"{i}{j}"
                if board_record[key] == player_value:
                    counter += 1
            if counter == self.__size:
                return True
            else:
                counter = 0
        return False

    def check_if_someone_wins_cross_diagonally(
        self, player_value: str, board_record: dict
    ) -> bool:
        counter1 = 0
        counter2 = 0
        for i in range(self.__size):
            key1 = f"{self.__needed_part_of_alphabet[i] + str(i + 1)}"
            key2 = f"{self.__needed_part_of_alphabet[self.__size - 1 - i] + str(i + 1)}"
            if board_record[key1] == player_value:
                counter1 += 1
            if board_record[key2] == player_value:
                counter2 += 1
        if counter1 == self.__size or counter2 == self.__size:
            return True
        return False
