def draw_header(part_of_alphabet):
    line_identifier = "0. "
    header = f"{line_identifier}"
    
    for i in range(len(part_of_alphabet)):
        header += "| " + part_of_alphabet[i] + " "

    header += "|"
    print(header)
    draw_separator(line_identifier, header)


def draw_body(part_of_alphabet, board):
    row = ""
    for i in range(len(part_of_alphabet)):
        helper_index = i + 1
        line_identifier = f"{helper_index}. "
        part_of_row = ""
        for j in part_of_alphabet:
            element = board[(j + str(helper_index))]
            part_of_row += f"| {element} "
        row = f"{line_identifier}{part_of_row}|"
        print(row)
    draw_separator(line_identifier, row)


def draw_separator(line_identifier, countable_body):
    len_line_identifier = len(line_identifier)
    length_of_dashes = len(countable_body) - len_line_identifier
    print(" " * len_line_identifier + "-" * length_of_dashes)


def draw_board(part_of_alphabet, board):
    draw_header(part_of_alphabet)
    draw_body(part_of_alphabet, board)