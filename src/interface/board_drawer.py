from interface.colors import Colors


class BoardDrawer:
    def draw_header(self, part_of_alphabet: list) -> None:
        line_identifier = "0. "
        header = f"{line_identifier}"

        for i in range(len(part_of_alphabet)):
            header += "| " + part_of_alphabet[i] + " "

        header += "|"
        print(header)
        self.draw_separator(line_identifier, len(part_of_alphabet))

    def draw_body(self, part_of_alphabet: list, board: dict) -> None:
        row = ""
        for i in range(len(part_of_alphabet)):
            helper_index = i + 1
            line_identifier = f"{helper_index}. "
            part_of_row = ""
            for j in part_of_alphabet:
                element = board[(j + str(helper_index))]
                sub_colored_element = (
                    Colors.WARNING + element + Colors.END if element == "O" else element
                )
                colored_element = (
                    Colors.BLUE + element + Colors.END
                    if element == "X"
                    else sub_colored_element
                )
                part_of_row += f"| {colored_element} "
            row = f"{line_identifier}{part_of_row}|"
            print(row)
        self.draw_separator(line_identifier, len(part_of_alphabet))

    def draw_separator(self, line_identifier: str, size: int) -> None:
        len_line_identifier = len(line_identifier)
        length_of_dashes = size * 4 + 1
        print(" " * len_line_identifier + "-" * length_of_dashes)

    def draw_board(self, part_of_alphabet: list, board: dict) -> None:
        self.draw_header(part_of_alphabet)
        self.draw_body(part_of_alphabet, board)
