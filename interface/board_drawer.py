import string


board_size_swithcer = {"a": 3, "b": 5, "c": 7}
alphabet = list(string.ascii_lowercase)


def draw_header(size):
    line_identifier = "0. "
    header = f"{line_identifier}"
    
    for i in range(size):
        header += "| " + alphabet[i] + " "

    header += "|"
    print(header)
    draw_separator(line_identifier, header)


def draw_body(size):
    row = ""
    for i in range(1, size + 1):
        line_identifier = f"{i}. "
        part_of_row = "| x " * size
        row = f"{line_identifier}{part_of_row}|"
        print(row)
    draw_separator(line_identifier, row)


def draw_separator(line_identifier, countable_body):
    len_line_identifier = len(line_identifier)
    length_of_dashes = len(countable_body) - len_line_identifier
    print(" " * len_line_identifier + "-" * length_of_dashes)


def draw_board(board_size_chosen_option):
    size = board_size_swithcer[board_size_chosen_option]
    draw_header(size)
    draw_body(size)