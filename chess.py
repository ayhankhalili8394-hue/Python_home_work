import turtle
from copy import deepcopy

# start

screen = turtle.Screen()
screen.title("Chess Game")
screen.setup(width=1000, height=850)
screen.bgcolor("#202020")
screen.tracer(0)

selected_difficulty = None
selected_color = None

buttons = []

selected_square = None
possible_moves = []

turn = "white"

en_passant_target = None

white_king_moved = False
black_king_moved = False

white_rook_a_moved = False
white_rook_h_moved = False
black_rook_a_moved = False
black_rook_h_moved = False

game_over = False

board_size = 640
square_size = 80

board_left = -320
board_bottom = -300

title = turtle.Turtle()
title.hideturtle()
title.penup()

drawing = turtle.Turtle()
drawing.hideturtle()
drawing.penup()

pieces_writer = turtle.Turtle()
pieces_writer.hideturtle()
pieces_writer.penup()

highlight_writer = turtle.Turtle()
highlight_writer.hideturtle()
highlight_writer.penup()

coordinates_writer = turtle.Turtle()
coordinates_writer.hideturtle()
coordinates_writer.penup()

message_writer = turtle.Turtle()
message_writer.hideturtle()
message_writer.penup()


WHITE_SYMBOLS = {
    "♔", "♕", "♖", "♗", "♘", "♙"
}

BLACK_SYMBOLS = {
    "♚", "♛", "♜", "♝", "♞", "♟"
}


PIECE_TO_TYPE = {
    "♔": "K",
    "♕": "Q",
    "♖": "R",
    "♗": "B",
    "♘": "N",
    "♙": "P",

    "♚": "K",
    "♛": "Q",
    "♜": "R",
    "♝": "B",
    "♞": "N",
    "♟": "P"
}


chess_board = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
]


def show_title(text, y=350, size=32):

    title.clear()
    title.color("white")
    title.goto(0, y)

    title.write(
        text,
        align="center",
        font=("Arial", size, "bold")
    )


def create_button(text, y):

    button = turtle.Turtle()
    button.hideturtle()
    button.penup()

    button.goto(-180, y)

    button.color("white")
    button.fillcolor("#404040")

    button.begin_fill()

    for _ in range(2):
        button.forward(360)
        button.right(90)
        button.forward(55)
        button.right(90)

    button.end_fill()

    button.goto(0, y - 40)

    button.color("white")

    button.write(
        text,
        align="center",
        font=("Arial", 18, "bold")
    )

    buttons.append(
        (button, text, y)
    )


def clear_buttons():

    global buttons

    for button, text, y in buttons:
        button.clear()
        button.hideturtle()

    buttons = []


def difficulty_screen():

    clear_buttons()

    show_title("CHESS GAME")

    difficulties = [
        "EASY",
        "MEDIUM",
        "HARD",
        "INSANE",
        "IMPOSSIBLE",
        "IRAN MODE"
    ]

    for i, difficulty in enumerate(difficulties):

        create_button(
            difficulty,
            180 - i * 65
        )

    screen.update()


def color_screen():

    clear_buttons()

    show_title("CHOOSE YOUR SIDE")

    info = turtle.Turtle()
    info.hideturtle()
    info.penup()
    info.color("white")
    info.goto(0, 225)

    info.write(
        "Difficulty: " + selected_difficulty,
        align="center",
        font=("Arial", 16, "normal")
    )

    create_button("WHITE", 120)
    create_button("BLACK", 20)

    screen.update()

# board

def draw_board():

    drawing.clear()

    light = "#F0D9B5"
    dark = "#B58863"

    for row in range(8):

        for col in range(8):

            x = board_left + col * square_size
            y = board_bottom + row * square_size

            drawing.goto(x, y)

            if (row + col) % 2 == 0:
                drawing.color(light)
                drawing.fillcolor(light)
            else:
                drawing.color(dark)
                drawing.fillcolor(dark)

            drawing.begin_fill()

            for _ in range(4):
                drawing.forward(square_size)
                drawing.left(90)

            drawing.end_fill()


def draw_pieces():

    pieces_writer.clear()

    for row in range(8):

        for col in range(8):

            piece = chess_board[row][col]

            if piece == "":
                continue

            x = (
                board_left
                + col * square_size
                + square_size / 2
            )

            y = (
                board_bottom
                + row * square_size
                + 8
            )

            pieces_writer.goto(x, y)

            if piece in BLACK_SYMBOLS:
                pieces_writer.color("black")
            else:
                pieces_writer.color("white")

            pieces_writer.write(
                piece,
                align="center",
                font=("DejaVu Sans", 48, "normal")
            )


def draw_coordinates():

    coordinates_writer.clear()
    coordinates_writer.color("white")

    files = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h"
    ]

    for col in range(8):

        x = (
            board_left
            + col * square_size
            + square_size / 2
        )

        coordinates_writer.goto(
            x,
            board_bottom - 25
        )

        coordinates_writer.write(
            files[col],
            align="center",
            font=("Arial", 12, "bold")
        )

    for row in range(8):

        y = (
            board_bottom
            + row * square_size
            + square_size / 2
            - 5
        )

        coordinates_writer.goto(
            board_left - 25,
            y
        )

        coordinates_writer.write(
            str(row + 1),
            align="center",
            font=("Arial", 12, "bold")
        )


# position

def get_board_position(x, y):

    col = int(
        (x - board_left)
        // square_size
    )

    row = int(
        (y - board_bottom)
        // square_size
    )

    if not (0 <= row < 8):
        return None

    if not (0 <= col < 8):
        return None

    return row, col


def inside(row, col):

    return (
        0 <= row < 8
        and
        0 <= col < 8
    )


def is_white(piece):

    return piece in WHITE_SYMBOLS


def is_black(piece):

    return piece in BLACK_SYMBOLS


def other_color(color):

    if color == "white":
        return "black"

    return "white"


def piece_is_color(piece, color):

    if color == "white":
        return is_white(piece)

    return is_black(piece)


def opponent_piece(piece, color):

    if piece == "":
        return False

    if color == "white":
        return is_black(piece)

    return is_white(piece)

# movement

def knight_attacks(row, col):

    moves = []

    directions = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1)
    ]

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        if inside(r, c):
            moves.append((r, c))

    return moves


def king_attacks(row, col):

    moves = []

    for dr in (-1, 0, 1):

        for dc in (-1, 0, 1):

            if dr == 0 and dc == 0:
                continue

            r = row + dr
            c = col + dc

            if inside(r, c):
                moves.append((r, c))

    return moves


def sliding_moves(
    board,
    row,
    col,
    color,
    directions
):

    moves = []

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        while inside(r, c):

            target = board[r][c]

            if target == "":

                moves.append((r, c))

            else:

                if opponent_piece(
                    target,
                    color
                ):

                    moves.append((r, c))

                break

            r += dr
            c += dc

    return moves


def pawn_moves(
    board,
    row,
    col,
    color,
    ep_target
):

    moves = []

    if color == "white":

        direction = -1
        start_row = 6

    else:

        direction = 1
        start_row = 1

    one_row = row + direction

    # one square forward

    if inside(one_row, col):

        if board[one_row][col] == "":

            moves.append(
                (one_row, col)
            )

            # two squares from starting position

            two_row = row + direction * 2

            if (
                row == start_row
                and board[two_row][col] == ""
            ):

                moves.append(
                    (two_row, col)
                )

    # diagonal captures

    for dc in (-1, 1):

        new_col = col + dc

        if not inside(
            one_row,
            new_col
        ):
            continue

        target = board[
            one_row
        ][
            new_col
        ]

        if opponent_piece(
            target,
            color
        ):

            moves.append(
                (one_row, new_col)
            )

        # en passant

        elif ep_target == (
            one_row,
            new_col
        ):

            moves.append(
                (one_row, new_col)
            )

    return moves


def pseudo_moves(
    board,
    row,
    col,
    color,
    ep_target
):

    piece = board[row][col]

    if piece == "":
        return []

    if not piece_is_color(
        piece,
        color
    ):
        return []

    piece_type = PIECE_TO_TYPE[piece]

    # pawn

    if piece_type == "P":

        return pawn_moves(
            board,
            row,
            col,
            color,
            ep_target
        )

    # knight

    if piece_type == "N":

        moves = []

        for r, c in knight_attacks(
            row,
            col
        ):

            target = board[r][c]

            if target == "":

                moves.append((r, c))

            elif opponent_piece(
                target,
                color
            ):

                moves.append((r, c))

        return moves

    # bishop

    if piece_type == "B":

        return sliding_moves(
            board,
            row,
            col,
            color,
            [
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1)
            ]
        )

    # rook

    if piece_type == "R":

        return sliding_moves(
            board,
            row,
            col,
            color,
            [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]
        )

    # queen

    if piece_type == "Q":

        return sliding_moves(
            board,
            row,
            col,
            color,
            [
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1),
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]
        )

    # king

    if piece_type == "K":

        moves = []

        for r, c in king_attacks(
            row,
            col
        ):

            target = board[r][c]

            if target == "":

                moves.append((r, c))

            elif opponent_piece(
                target,
                color
            ):

                moves.append((r, c))

        return moves

    return []


# find king

def find_king(board, color):

    if color == "white":
        king = "♔"
    else:
        king = "♚"

    for row in range(8):

        for col in range(8):

            if board[row][col] == king:

                return row, col

    return None


# attacked squares

def square_attacked(
    board,
    row,
    col,
    attacking_color
):

    # pawn attacks

    if attacking_color == "white":

        pawn_row = row - 1
        pawn = "♙"

    else:

        pawn_row = row + 1
        pawn = "♟"

    for dc in (-1, 1):

        pawn_col = col + dc

        if inside(
            pawn_row,
            pawn_col
        ):

            if (
                board[pawn_row][pawn_col]
                == pawn
            ):

                return True

    # knight attacks

    knight = (
        "♘"
        if attacking_color == "white"
        else "♞"
    )

    for r in range(8):

        for c in range(8):

            if board[r][c] == knight:

                if (
                    row,
                    col
                ) in knight_attacks(
                    r,
                    c
                ):

                    return True

    # king attacks

    king = (
        "♔"
        if attacking_color == "white"
        else "♚"
    )

    for r in range(8):

        for c in range(8):

            if board[r][c] == king:

                if (
                    row,
                    col
                ) in king_attacks(
                    r,
                    c
                ):

                    return True

    # bishop and queen attacks

    bishop = (
        "♗"
        if attacking_color == "white"
        else "♝"
    )

    queen = (
        "♕"
        if attacking_color == "white"
        else "♛"
    )

    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        while inside(r, c):

            piece = board[r][c]

            if piece != "":

                if (
                    piece == bishop
                    or piece == queen
                ):

                    return True

                break

            r += dr
            c += dc

    # rook and queen attacks

    rook = (
        "♖"
        if attacking_color == "white"
        else "♜"
    )

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        while inside(r, c):

            piece = board[r][c]

            if piece != "":

                if (
                    piece == rook
                    or piece == queen
                ):

                    return True

                break

            r += dr
            c += dc

    return False


def in_check(board, color):

    king_position = find_king(
        board,
        color
    )

    if king_position is None:
        return True

    row, col = king_position

    return square_attacked(
        board,
        row,
        col,
        other_color(color)
    )

# legal moves

def simulate_move(
    board,
    start,
    end,
    ep_target
):

    new_board = deepcopy(board)

    sr, sc = start
    er, ec = end

    piece = new_board[sr][sc]

    # en passant capture

    if (
        PIECE_TO_TYPE.get(piece) == "P"
        and ep_target == end
        and sc != ec
        and new_board[er][ec] == ""
    ):

        if piece == "♙":
            capture_row = er - 1
        else:
            capture_row = er + 1

        new_board[capture_row][ec] = ""

    # normal move

    new_board[er][ec] = piece
    new_board[sr][sc] = ""

    # castling

    if (
        piece == "♔"
        and sr == 0
        and sc == 4
        and er == 0
        and ec == 6
    ):

        new_board[0][5] = new_board[0][7]
        new_board[0][7] = ""

    elif (
        piece == "♔"
        and sr == 0
        and sc == 4
        and er == 0
        and ec == 2
    ):

        new_board[0][3] = new_board[0][0]
        new_board[0][0] = ""

    elif (
        piece == "♚"
        and sr == 7
        and sc == 4
        and er == 7
        and ec == 6
    ):

        new_board[7][5] = new_board[7][7]
        new_board[7][7] = ""

    elif (
        piece == "♚"
        and sr == 7
        and sc == 4
        and er == 7
        and ec == 2
    ):

        new_board[7][3] = new_board[7][0]
        new_board[7][0] = ""

    return new_board


def castling_moves(
    board,
    color
):

    moves = []

    if color == "white":

        row = 0

        # kingside

        if (
            not white_king_moved
            and not white_rook_h_moved
            and board[row][4] == "♔"
            and board[row][7] == "♖"
            and board[row][5] == ""
            and board[row][6] == ""
            and not in_check(
                board,
                "white"
            )
            and not square_attacked(
                board,
                row,
                5,
                "black"
            )
            and not square_attacked(
                board,
                row,
                6,
                "black"
            )
        ):

            moves.append((row, 6))

        # queenside

        if (
            not white_king_moved
            and not white_rook_a_moved
            and board[row][4] == "♔"
            and board[row][0] == "♖"
            and board[row][1] == ""
            and board[row][2] == ""
            and board[row][3] == ""
            and not in_check(
                board,
                "white"
            )
            and not square_attacked(
                board,
                row,
                3,
                "black"
            )
            and not square_attacked(
                board,
                row,
                2,
                "black"
            )
        ):

            moves.append((row, 2))

    else:

        row = 7

        # kingside

        if (
            not black_king_moved
            and not black_rook_h_moved
            and board[row][4] == "♚"
            and board[row][7] == "♜"
            and board[row][5] == ""
            and board[row][6] == ""
            and not in_check(
                board,
                "black"
            )
            and not square_attacked(
                board,
                row,
                5,
                "white"
            )
            and not square_attacked(
                board,
                row,
                6,
                "white"
            )
        ):

            moves.append((row, 6))

        # queenside

        if (
            not black_king_moved
            and not black_rook_a_moved
            and board[row][4] == "♚"
            and board[row][0] == "♜"
            and board[row][1] == ""
            and board[row][2] == ""
            and board[row][3] == ""
            and not in_check(
                board,
                "black"
            )
            and not square_attacked(
                board,
                row,
                3,
                "white"
            )
            and not square_attacked(
                board,
                row,
                2,
                "white"
            )
        ):

            moves.append((row, 2))

    return moves


def legal_moves_for_piece(
    board,
    row,
    col,
    color,
    ep_target
):

    piece = board[row][col]

    if piece == "":
        return []

    if not piece_is_color(
        piece,
        color
    ):
        return []

    moves = pseudo_moves(
        board,
        row,
        col,
        color,
        ep_target
    )

    # castling

    if PIECE_TO_TYPE[piece] == "K":

        moves += castling_moves(
            board,
            color
        )

    legal_moves = []

    for move in moves:

        new_board = simulate_move(
            board,
            (row, col),
            move,
            ep_target
        )

        if not in_check(
            new_board,
            color
        ):

            legal_moves.append(
                move
            )

    # remove duplicates

    return list(
        dict.fromkeys(
            legal_moves
        )
    )


def all_legal_moves(
    board,
    color,
    ep_target
):

    moves = []

    for row in range(8):

        for col in range(8):

            piece = board[row][col]

            if piece == "":
                continue

            if not piece_is_color(
                piece,
                color
            ):
                continue

            piece_moves = legal_moves_for_piece(
                board,
                row,
                col,
                color,
                ep_target
            )

            for move in piece_moves:

                moves.append(
                    (
                        (row, col),
                        move
                    )
                )

    return moves


def is_checkmate(
    board,
    color,
    ep_target
):

    if not in_check(
        board,
        color
    ):

        return False

    return len(
        all_legal_moves(
            board,
            color,
            ep_target
        )
    ) == 0


def is_stalemate(
    board,
    color,
    ep_target
):

    if in_check(
        board,
        color
    ):

        return False

    return len(
        all_legal_moves(
            board,
            color,
            ep_target
        )
    ) == 0


# make real move

def apply_move(
    start,
    end
):

    global en_passant_target
    global white_king_moved
    global black_king_moved
    global white_rook_a_moved
    global white_rook_h_moved
    global black_rook_a_moved
    global black_rook_h_moved
    global turn

    sr, sc = start
    er, ec = end

    piece = chess_board[sr][sc]
    captured = chess_board[er][ec]

    # en passant

    if (
        PIECE_TO_TYPE.get(piece) == "P"
        and en_passant_target == end
        and sc != ec
        and captured == ""
    ):

        if piece == "♙":
            capture_row = er - 1
        else:
            capture_row = er + 1

        chess_board[capture_row][ec] = ""

        captured = (
            "♟"
            if piece == "♙"
            else "♙"
        )

    chess_board[er][ec] = piece
    chess_board[sr][sc] = ""

    # king

    if piece == "♔":

        white_king_moved = True

        # white kingside castle

        if (
            sr == 0
            and sc == 4
            and er == 0
            and ec == 6
        ):

            chess_board[0][5] = chess_board[0][7]
            chess_board[0][7] = ""

            white_rook_h_moved = True

        # white queenside castle

        elif (
            sr == 0
            and sc == 4
            and er == 0
            and ec == 2
        ):

            chess_board[0][3] = chess_board[0][0]
            chess_board[0][0] = ""

            white_rook_a_moved = True

    elif piece == "♚":

        black_king_moved = True

        # black kingside castle

        if (
            sr == 7
            and sc == 4
            and er == 7
            and ec == 6
        ):

            chess_board[7][5] = chess_board[7][7]
            chess_board[7][7] = ""

            black_rook_h_moved = True

        # black queenside castle

        elif (
            sr == 7
            and sc == 4
            and er == 7
            and ec == 2
        ):

            chess_board[7][3] = chess_board[7][0]
            chess_board[7][0] = ""

            black_rook_a_moved = True

    # rook movement

    if piece == "♖":

        if sr == 0 and sc == 0:
            white_rook_a_moved = True

        elif sr == 0 and sc == 7:
            white_rook_h_moved = True

    elif piece == "♜":

        if sr == 7 and sc == 0:
            black_rook_a_moved = True

        elif sr == 7 and sc == 7:
            black_rook_h_moved = True

    # rook captured

    if captured == "♖":

        if er == 0 and ec == 0:
            white_rook_a_moved = True

        elif er == 0 and ec == 7:
            white_rook_h_moved = True

    elif captured == "♜":

        if er == 7 and ec == 0:
            black_rook_a_moved = True

        elif er == 7 and ec == 7:
            black_rook_h_moved = True

    # en passant target

    en_passant_target = None

    if (
        piece == "♙"
        and sr == 1
        and er == 3
    ):

        en_passant_target = (
            2,
            sc
        )

    elif (
        piece == "♟"
        and sr == 6
        and er == 4
    ):

        en_passant_target = (
            5,
            sc
        )

    # promotion

    if piece == "♙" and er == 7:

        chess_board[er][ec] = "♕"

    elif piece == "♟" and er == 0:

        chess_board[er][ec] = "♛"

    turn = other_color(turn)

# highlights

def move_would_be_check_or_mate(
    start,
    end,
    color
):

    test_board = simulate_move(
        chess_board,
        start,
        end,
        en_passant_target
    )

    enemy = other_color(color)

    if not in_check(
        test_board,
        enemy
    ):
        return None

    if len(
        all_legal_moves(
            test_board,
            enemy,
            None
        )
    ) == 0:

        return "mate"

    return "check"


def move_can_be_captured(
    start,
    end,
    color
):

    test_board = simulate_move(
        chess_board,
        start,
        end,
        en_passant_target
    )

    enemy = other_color(color)

    enemy_moves = all_legal_moves(
        test_board,
        enemy,
        None
    )

    for enemy_start, enemy_end in enemy_moves:

        if enemy_end == end:
            return True

    return False


def get_highlight_color(
    start,
    end
):

    sr, sc = start

    piece = chess_board[sr][sc]

    color = (
        "white"
        if is_white(piece)
        else "black"
    )

    target = chess_board[
        end[0]
    ][
        end[1]
    ]

    result = move_would_be_check_or_mate(
        start,
        end,
        color
    )

    # checkmate

    if result == "mate":

        return "#A020F0"

    # check

    if result == "check":

        return "#3399FF"

    # capture

    if target != "":

        return "#FF4444"

    # opponent can capture this piece

    if move_can_be_captured(
        start,
        end,
        color
    ):

        return "#FFD700"

    # normal legal move

    return "#66CC66"


def draw_highlights():

    highlight_writer.clear()

    if selected_square is None:
        return

    for row, col in possible_moves:

        x = (
            board_left
            + col * square_size
            + square_size / 2
        )

        y = (
            board_bottom
            + row * square_size
            + square_size / 2
        )

        highlight_writer.goto(
            x,
            y
        )

        highlight_writer.color(
            get_highlight_color(
                selected_square,
                (row, col)
            )
        )

        # small dot instead of covering the square

        highlight_writer.dot(18)


# message

def show_message(text):

    message_writer.clear()

    message_writer.color("white")

    message_writer.goto(
        0,
        365
    )

    message_writer.write(
        text,
        align="center",
        font=(
            "Arial",
            18,
            "bold"
        )
    )


# chess screen

def chess_screen():

    clear_buttons()

    title.clear()

    message_writer.clear()

    draw_board()

    draw_pieces()

    draw_coordinates()

    screen.update()


# difficulty click

def difficulty_click(
    x,
    y
):

    global selected_difficulty

    for (
        button,
        difficulty,
        button_y
    ) in buttons:

        if (
            -180 <= x <= 180
            and
            button_y - 55 <= y <= button_y
        ):

            selected_difficulty = difficulty

            color_screen()

            return


# color click

def color_click(
    x,
    y
):

    global selected_color
    global turn

    for (
        button,
        color,
        button_y
    ) in buttons:

        if (
            -180 <= x <= 180
            and
            button_y - 55 <= y <= button_y
        ):

            selected_color = color

            turn = "white"

            chess_screen()

            return


# board click

def board_click(
    x,
    y
):

    global selected_square
    global possible_moves
    global game_over

    if game_over:
        return

    position = get_board_position(
        x,
        y
    )

    if position is None:
        return

    row, col = position

    # a piece is already selected

    if selected_square is not None:

        # clicked on a legal destination

        if position in possible_moves:

            apply_move(
                selected_square,
                position
            )

            selected_square = None
            possible_moves = []

            draw_highlights()
            draw_pieces()

            # checkmate

            if is_checkmate(
                chess_board,
                turn,
                en_passant_target
            ):

                game_over = True

                winner = other_color(turn)

                show_message(
                    "CHECKMATE - "
                    + winner.upper()
                    + " WINS"
                )

            # stalemate

            elif is_stalemate(
                chess_board,
                turn,
                en_passant_target
            ):

                game_over = True

                show_message(
                    "STALEMATE"
                )

            # check

            elif in_check(
                chess_board,
                turn
            ):

                show_message(
                    turn.upper()
                    + " IS IN CHECK"
                )

            else:

                message_writer.clear()

            screen.update()

            return

        # click another own piece

        piece = chess_board[row][col]

        if (
            piece != ""
            and piece_is_color(
                piece,
                turn
            )
        ):

            selected_square = position

            possible_moves = legal_moves_for_piece(
                chess_board,
                row,
                col,
                turn,
                en_passant_target
            )

            draw_highlights()

            screen.update()

            return

        # click somewhere else

        selected_square = None
        possible_moves = []

        draw_highlights()

        screen.update()

        return

    # select a piece

    piece = chess_board[row][col]

    if piece == "":
        return

    if not piece_is_color(
        piece,
        turn
    ):

        return

    selected_square = position

    possible_moves = legal_moves_for_piece(
        chess_board,
        row,
        col,
        turn,
        en_passant_target
    )

    draw_highlights()

    screen.update()


# main click handler

def handle_click(
    x,
    y
):

    if selected_difficulty is None:

        difficulty_click(
            x,
            y
        )

    elif selected_color is None:

        color_click(
            x,
            y
        )

    else:

        board_click(
            x,
            y
        )


# bot foundation

import random
import time


def get_player_color():

    if selected_color == "WHITE":
        return "white"

    return "black"


def get_bot_color():

    if selected_color == "WHITE":
        return "black"

    return "white"


def bot_is_turn():

    if selected_color is None:
        return False

    return turn == get_bot_color()


def choose_random_move():

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:
        return None

    return random.choice(moves)


def make_bot_move():

    global selected_square
    global possible_moves
    global game_over

    if game_over:
        return

    if not bot_is_turn():
        return

    move = choose_random_move()

    if move is None:

        if is_checkmate(
            chess_board,
            turn,
            en_passant_target
        ):

            game_over = True

            show_message(
                "CHECKMATE - "
                + get_player_color().upper()
                + " WINS"
            )

        else:

            game_over = True

            show_message(
                "STALEMATE"
            )

        screen.update()

        return

    start, end = move

    apply_move(
        start,
        end
    )

    selected_square = None
    possible_moves = []

    draw_highlights()
    draw_pieces()

    if is_checkmate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "CHECKMATE - "
            + get_bot_color().upper()
            + " WINS"
        )

    elif is_stalemate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "STALEMATE"
        )

    elif in_check(
        chess_board,
        turn
    ):

        show_message(
            turn.upper()
            + " IS IN CHECK"
        )

    else:

        message_writer.clear()

    screen.update()


# bot connection

def bot_after_player_move():

    if game_over:
        return

    if bot_is_turn():

        screen.ontimer(
            make_bot_move,
            700
        )


def new_board_click(x, y):

    if game_over:
        return

    old_turn = turn

    board_click(x, y)

    if (
        old_turn != turn
        and not game_over
        and bot_is_turn()
    ):

        screen.ontimer(
            make_bot_move,
            700
        )


def new_handle_click(x, y):

    if selected_difficulty is None:

        difficulty_click(
            x,
            y
        )

    elif selected_color is None:

        color_click(
            x,
            y
        )

    else:

        new_board_click(
            x,
            y
        )

# bot start

def start_bot_if_needed():

    if selected_color is None:
        return

    if bot_is_turn():

        screen.ontimer(
            make_bot_move,
            700
        )


def new_color_click(x, y):

    global selected_color
    global turn

    for (
        button,
        color,
        button_y
    ) in buttons:

        if (
            -180 <= x <= 180
            and
            button_y - 55 <= y <= button_y
        ):

            selected_color = color

            turn = "white"

            chess_screen()

            start_bot_if_needed()

            return


def final_handle_click(x, y):

    if selected_difficulty is None:

        difficulty_click(
            x,
            y
        )

    elif selected_color is None:

        new_color_click(
            x,
            y
        )

    else:

        new_board_click(
            x,
            y
        )

# medium bot

PIECE_VALUES = {
    "P": 100,
    "N": 320,
    "B": 330,
    "R": 500,
    "Q": 900,
    "K": 20000
}


def get_piece_value(piece):

    if piece == "":
        return 0

    piece_type = PIECE_TO_TYPE[piece]

    return PIECE_VALUES[piece_type]


def move_capture_value(start, end):

    target = chess_board[
        end[0]
    ][
        end[1]
    ]

    if target == "":
        return 0

    return get_piece_value(target)


def move_gives_check(
    start,
    end
):

    piece = chess_board[
        start[0]
    ][
        start[1]
    ]

    color = (
        "white"
        if is_white(piece)
        else "black"
    )

    test_board = simulate_move(
        chess_board,
        start,
        end,
        en_passant_target
    )

    return in_check(
        test_board,
        other_color(color)
    )


def move_gives_mate(
    start,
    end
):

    piece = chess_board[
        start[0]
    ][
        start[1]
    ]

    color = (
        "white"
        if is_white(piece)
        else "black"
    )

    test_board = simulate_move(
        chess_board,
        start,
        end,
        en_passant_target
    )

    enemy = other_color(color)

    return is_checkmate(
        test_board,
        enemy,
        None
    )


def medium_move_score(
    start,
    end
):

    score = 0

    # checkmate is extremely valuable

    if move_gives_mate(
        start,
        end
    ):

        score += 100000

    # giving check

    elif move_gives_check(
        start,
        end
    ):

        score += 500

    # capturing pieces

    score += move_capture_value(
        start,
        end
    )

    # small bonus for moving toward the center

    row, col = end

    center_distance = (
        abs(row - 3.5)
        +
        abs(col - 3.5)
    )

    score += (
        20
        - center_distance * 3
    )

    # tiny randomness so equal moves aren't
    # always identical

    score += random.randint(
        0,
        10
    )

    return score


def choose_medium_move():

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:
        return None

    best_move = None
    best_score = -float("inf")

    for start, end in moves:

        score = medium_move_score(
            start,
            end
        )

        if score > best_score:

            best_score = score
            best_move = (
                start,
                end
            )

    return best_move


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    return choose_random_move()


def make_bot_move():

    global selected_square
    global possible_moves
    global game_over

    if game_over:
        return

    if not bot_is_turn():
        return

    move = choose_bot_move()

    if move is None:

        if is_checkmate(
            chess_board,
            turn,
            en_passant_target
        ):

            game_over = True

            show_message(
                "CHECKMATE - "
                + get_player_color().upper()
                + " WINS"
            )

        else:

            game_over = True

            show_message(
                "STALEMATE"
            )

        screen.update()

        return

    start, end = move

    apply_move(
        start,
        end
    )

    selected_square = None
    possible_moves = []

    draw_highlights()
    draw_pieces()

    if is_checkmate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "CHECKMATE - "
            + get_bot_color().upper()
            + " WINS"
        )

    elif is_stalemate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "STALEMATE"
        )

    elif in_check(
        chess_board,
        turn
    ):

        show_message(
            turn.upper()
            + " IS IN CHECK"
        )

    else:

        message_writer.clear()

    screen.update()

# hard bot

SEARCH_DEPTH_HARD = 2


def board_material_score(board, bot_color):

    score = 0

    for row in range(8):

        for col in range(8):

            piece = board[row][col]

            if piece == "":
                continue

            value = get_piece_value(piece)

            if piece_is_color(
                piece,
                bot_color
            ):

                score += value

            else:

                score -= value

    return score


def evaluate_board(
    board,
    bot_color
):

    score = board_material_score(
        board,
        bot_color
    )

    enemy = other_color(
        bot_color
    )

    # check is bad for the side being checked

    if in_check(
        board,
        bot_color
    ):

        score -= 80

    if in_check(
        board,
        enemy
    ):

        score += 80

    # checkmate

    if is_checkmate(
        board,
        enemy,
        None
    ):

        score += 100000

    if is_checkmate(
        board,
        bot_color,
        None
    ):

        score -= 100000

    return score


def minimax(
    board,
    color_to_move,
    bot_color,
    depth,
    alpha,
    beta,
    ep_target
):

    legal_moves = all_legal_moves(
        board,
        color_to_move,
        ep_target
    )

    # game over

    if len(legal_moves) == 0:

        if in_check(
            board,
            color_to_move
        ):

            if color_to_move == bot_color:

                return -100000 - depth

            return 100000 + depth

        return 0

    # stop searching

    if depth == 0:

        return evaluate_board(
            board,
            bot_color
        )

    maximizing = (
        color_to_move == bot_color
    )

    if maximizing:

        best_score = -float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                ep_target
            )

            score = minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta,
                None
            )

            best_score = max(
                best_score,
                score
            )

            alpha = max(
                alpha,
                score
            )

            if beta <= alpha:
                break

        return best_score

    else:

        best_score = float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                ep_target
            )

            score = minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta,
                None
            )

            best_score = min(
                best_score,
                score
            )

            beta = min(
                beta,
                score
            )

            if beta <= alpha:
                break

        return best_score


def choose_hard_move():

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:
        return None

    bot_color = get_bot_color()

    best_move = None
    best_score = -float("inf")

    for start, end in moves:

        new_board = simulate_move(
            chess_board,
            start,
            end,
            en_passant_target
        )

        score = minimax(
            new_board,
            other_color(turn),
            bot_color,
            SEARCH_DEPTH_HARD - 1,
            -float("inf"),
            float("inf"),
            None
        )

        if score > best_score:

            best_score = score
            best_move = (
                start,
                end
            )

    return best_move


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    if selected_difficulty == "HARD":

        return choose_hard_move()

    return choose_random_move()


def make_bot_move():

    global selected_square
    global possible_moves
    global game_over

    if game_over:
        return

    if not bot_is_turn():
        return

    move = choose_bot_move()

    if move is None:

        if is_checkmate(
            chess_board,
            turn,
            en_passant_target
        ):

            game_over = True

            show_message(
                "CHECKMATE - "
                + get_player_color().upper()
                + " WINS"
            )

        else:

            game_over = True

            show_message(
                "STALEMATE"
            )

        screen.update()

        return

    start, end = move

    apply_move(
        start,
        end
    )

    selected_square = None
    possible_moves = []

    draw_highlights()
    draw_pieces()

    if is_checkmate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "CHECKMATE - "
            + get_bot_color().upper()
            + " WINS"
        )

    elif is_stalemate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "STALEMATE"
        )

    elif in_check(
        chess_board,
        turn
    ):

        show_message(
            turn.upper()
            + " IS IN CHECK"
        )

    else:

        message_writer.clear()

    screen.update()

    # insane bot

SEARCH_DEPTH_INSANE = 3


def positional_score(
    board,
    bot_color
):

    score = 0

    for row in range(8):

        for col in range(8):

            piece = board[row][col]

            if piece == "":
                continue

            piece_type = PIECE_TO_TYPE[piece]

            center_distance = (
                abs(row - 3.5)
                +
                abs(col - 3.5)
            )

            center_bonus = (
                4 - center_distance
            ) * 4

            if piece_type == "P":
                bonus = 5
            elif piece_type == "N":
                bonus = center_bonus * 3
            elif piece_type == "B":
                bonus = center_bonus * 2
            elif piece_type == "Q":
                bonus = center_bonus
            else:
                bonus = 0

            if piece_is_color(
                piece,
                bot_color
            ):

                score += bonus

            else:

                score -= bonus

    return score


def insane_evaluate(
    board,
    bot_color
):

    score = evaluate_board(
        board,
        bot_color
    )

    score += positional_score(
        board,
        bot_color
    )

    enemy = other_color(
        bot_color
    )

    bot_moves = len(
        all_legal_moves(
            board,
            bot_color,
            None
        )
    )

    enemy_moves = len(
        all_legal_moves(
            board,
            enemy,
            None
        )
    )

    score += (
        bot_moves - enemy_moves
    ) * 3

    return score


def insane_minimax(
    board,
    color_to_move,
    bot_color,
    depth,
    alpha,
    beta
):

    legal_moves = all_legal_moves(
        board,
        color_to_move,
        None
    )

    if len(legal_moves) == 0:

        if in_check(
            board,
            color_to_move
        ):

            if color_to_move == bot_color:

                return -1000000

            return 1000000

        return 0

    if depth == 0:

        return insane_evaluate(
            board,
            bot_color
        )

    maximizing = (
        color_to_move == bot_color
    )

    if maximizing:

        best_score = -float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = insane_minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score > best_score:

                best_score = score

            if score > alpha:

                alpha = score

            if beta <= alpha:

                break

        return best_score

    else:

        best_score = float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = insane_minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score < best_score:

                best_score = score

            if score < beta:

                beta = score

            if beta <= alpha:

                break

        return best_score


def choose_insane_move():

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:

        return None

    bot_color = get_bot_color()

    best_move = None
    best_score = -float("inf")

    for start, end in moves:

        new_board = simulate_move(
            chess_board,
            start,
            end,
            en_passant_target
        )

        score = insane_minimax(
            new_board,
            other_color(turn),
            bot_color,
            SEARCH_DEPTH_INSANE - 1,
            -float("inf"),
            float("inf")
        )

        if score > best_score:

            best_score = score

            best_move = (
                start,
                end
            )

    return best_move


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    if selected_difficulty == "HARD":

        return choose_hard_move()

    if selected_difficulty == "INSANE":

        return choose_insane_move()

    return choose_random_move()


def make_bot_move():

    global selected_square
    global possible_moves
    global game_over

    if game_over:
        return

    if not bot_is_turn():
        return

    move = choose_bot_move()

    if move is None:

        if is_checkmate(
            chess_board,
            turn,
            en_passant_target
        ):

            game_over = True

            show_message(
                "CHECKMATE - "
                + get_player_color().upper()
                + " WINS"
            )

        else:

            game_over = True

            show_message(
                "STALEMATE"
            )

        screen.update()

        return

    start, end = move

    apply_move(
        start,
        end
    )

    selected_square = None
    possible_moves = []

    draw_highlights()
    draw_pieces()

    if is_checkmate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "CHECKMATE - "
            + get_bot_color().upper()
            + " WINS"
        )

    elif is_stalemate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "STALEMATE"
        )

    elif in_check(
        chess_board,
        turn
    ):

        show_message(
            turn.upper()
            + " IS IN CHECK"
        )

    else:

        message_writer.clear()

    screen.update()

# impossible bot

SEARCH_DEPTH_IMPOSSIBLE = 4


def move_priority(
    board,
    move
):

    start, end = move

    piece = board[
        start[0]
    ][
        start[1]
    ]

    target = board[
        end[0]
    ][
        end[1]
    ]

    score = 0

    # checkmate

    test_board = simulate_move(
        board,
        start,
        end,
        None
    )

    moving_color = (
        "white"
        if is_white(piece)
        else "black"
    )

    enemy = other_color(
        moving_color
    )

    if is_checkmate(
        test_board,
        enemy,
        None
    ):

        score += 1000000

    # captures

    if target != "":

        score += (
            get_piece_value(target)
            * 10
            - get_piece_value(piece)
        )

    # checks

    if in_check(
        test_board,
        enemy
    ):

        score += 5000

    # promotions

    if (
        PIECE_TO_TYPE.get(piece) == "P"
        and end[0] in (0, 7)
    ):

        score += 8000

    # center control

    center_distance = (
        abs(end[0] - 3.5)
        +
        abs(end[1] - 3.5)
    )

    score += (
        20 - center_distance
    )

    return score


def order_moves(
    board,
    moves
):

    scored_moves = []

    for move in moves:

        score = move_priority(
            board,
            move
        )

        scored_moves.append(
            (
                score,
                move
            )
        )

    scored_moves.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        move
        for score, move
        in scored_moves
    ]


def impossible_evaluate(
    board,
    bot_color
):

    score = insane_evaluate(
        board,
        bot_color
    )

    enemy = other_color(
        bot_color
    )

    # king safety

    if in_check(
        board,
        bot_color
    ):

        score -= 300

    if in_check(
        board,
        enemy
    ):

        score += 300

    # mobility

    bot_moves = len(
        all_legal_moves(
            board,
            bot_color,
            None
        )
    )

    enemy_moves = len(
        all_legal_moves(
            board,
            enemy,
            None
        )
    )

    score += (
        bot_moves - enemy_moves
    ) * 5

    return score


def impossible_minimax(
    board,
    color_to_move,
    bot_color,
    depth,
    alpha,
    beta
):

    legal_moves = all_legal_moves(
        board,
        color_to_move,
        None
    )

    if len(legal_moves) == 0:

        if in_check(
            board,
            color_to_move
        ):

            if color_to_move == bot_color:

                return -10000000 + depth

            return 10000000 - depth

        return 0

    if depth == 0:

        return impossible_evaluate(
            board,
            bot_color
        )

    legal_moves = order_moves(
        board,
        legal_moves
    )

    maximizing = (
        color_to_move == bot_color
    )

    if maximizing:

        best_score = -float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = impossible_minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score > best_score:

                best_score = score

            if score > alpha:

                alpha = score

            if beta <= alpha:

                break

        return best_score

    else:

        best_score = float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = impossible_minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score < best_score:

                best_score = score

            if score < beta:

                beta = score

            if beta <= alpha:

                break

        return best_score


def choose_impossible_move():

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:

        return None

    moves = order_moves(
        chess_board,
        moves
    )

    bot_color = get_bot_color()

    best_move = moves[0]

    best_score = -float("inf")

    for start, end in moves:

        new_board = simulate_move(
            chess_board,
            start,
            end,
            en_passant_target
        )

        score = impossible_minimax(
            new_board,
            other_color(turn),
            bot_color,
            SEARCH_DEPTH_IMPOSSIBLE - 1,
            -float("inf"),
            float("inf")
        )

        if score > best_score:

            best_score = score

            best_move = (
                start,
                end
            )

    return best_move


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    if selected_difficulty == "HARD":

        return choose_hard_move()

    if selected_difficulty == "INSANE":

        return choose_insane_move()

    if selected_difficulty == "IMPOSSIBLE":

        return choose_impossible_move()

    return choose_random_move()


def make_bot_move():

    global selected_square
    global possible_moves
    global game_over

    if game_over:
        return

    if not bot_is_turn():
        return

    move = choose_bot_move()

    if move is None:

        if is_checkmate(
            chess_board,
            turn,
            en_passant_target
        ):

            game_over = True

            show_message(
                "CHECKMATE - "
                + get_player_color().upper()
                + " WINS"
            )

        else:

            game_over = True

            show_message(
                "STALEMATE"
            )

        screen.update()

        return

    start, end = move

    apply_move(
        start,
        end
    )

    selected_square = None
    possible_moves = []

    draw_highlights()
    draw_pieces()

    if is_checkmate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "CHECKMATE - "
            + get_bot_color().upper()
            + " WINS"
        )

    elif is_stalemate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "STALEMATE"
        )

    elif in_check(
        chess_board,
        turn
    ):

        show_message(
            turn.upper()
            + " IS IN CHECK"
        )

    else:

        message_writer.clear()

    screen.update()

# iran mode

SEARCH_DEPTH_IRAN = 4


def iran_evaluate(
    board,
    bot_color
):

    score = impossible_evaluate(
        board,
        bot_color
    )

    enemy = other_color(
        bot_color
    )

    # Strong bonus for attacking the enemy king

    enemy_king = find_king(
        board,
        enemy
    )

    if enemy_king is not None:

        king_row, king_col = enemy_king

        attacks = 0

        for row in range(8):

            for col in range(8):

                piece = board[row][col]

                if piece == "":
                    continue

                if not piece_is_color(
                    piece,
                    bot_color
                ):
                    continue

                piece_moves = pseudo_moves(
                    board,
                    row,
                    col,
                    bot_color,
                    None
                )

                if (
                    king_row,
                    king_col
                ) in piece_moves:

                    attacks += 1

        score += attacks * 100

    # Protect valuable pieces

    for row in range(8):

        for col in range(8):

            piece = board[row][col]

            if piece == "":
                continue

            if not piece_is_color(
                piece,
                bot_color
            ):
                continue

            value = get_piece_value(
                piece
            )

            if value < 500:
                continue

            if square_attacked(
                board,
                row,
                col,
                enemy
            ):

                score -= value // 2

    return score


def iran_minimax(
    board,
    color_to_move,
    bot_color,
    depth,
    alpha,
    beta
):

    legal_moves = all_legal_moves(
        board,
        color_to_move,
        None
    )

    if len(legal_moves) == 0:

        if in_check(
            board,
            color_to_move
        ):

            if color_to_move == bot_color:

                return -10000000

            return 10000000

        return 0

    if depth == 0:

        return iran_evaluate(
            board,
            bot_color
        )

    legal_moves = order_moves(
        board,
        legal_moves
    )

    maximizing = (
        color_to_move == bot_color
    )

    if maximizing:

        best_score = -float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = iran_minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score > best_score:

                best_score = score

            if score > alpha:

                alpha = score

            if beta <= alpha:

                break

        return best_score

    else:

        best_score = float("inf")

        for start, end in legal_moves:

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = iran_minimax(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score < best_score:

                best_score = score

            if score < beta:

                beta = score

            if beta <= alpha:

                break

        return best_score


def choose_iran_move():

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:

        return None

    moves = order_moves(
        chess_board,
        moves
    )

    bot_color = get_bot_color()

    best_score = -float("inf")

    best_moves = []

    for start, end in moves:

        new_board = simulate_move(
            chess_board,
            start,
            end,
            en_passant_target
        )

        score = iran_minimax(
            new_board,
            other_color(turn),
            bot_color,
            SEARCH_DEPTH_IRAN - 1,
            -float("inf"),
            float("inf")
        )

        if score > best_score:

            best_score = score

            best_moves = [
                (start, end)
            ]

        elif score == best_score:

            best_moves.append(
                (start, end)
            )

    return random.choice(
        best_moves
    )


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    if selected_difficulty == "HARD":

        return choose_hard_move()

    if selected_difficulty == "INSANE":

        return choose_insane_move()

    if selected_difficulty == "IMPOSSIBLE":

        return choose_impossible_move()

    if selected_difficulty == "IRAN MODE":

        return choose_iran_move()

    return choose_random_move()


def make_bot_move():

    global selected_square
    global possible_moves
    global game_over

    if game_over:
        return

    if not bot_is_turn():
        return

    move = choose_bot_move()

    if move is None:

        if is_checkmate(
            chess_board,
            turn,
            en_passant_target
        ):

            game_over = True

            show_message(
                "CHECKMATE - "
                + get_player_color().upper()
                + " WINS"
            )

        else:

            game_over = True

            show_message(
                "STALEMATE"
            )

        screen.update()

        return

    start, end = move

    apply_move(
        start,
        end
    )

    selected_square = None
    possible_moves = []

    draw_highlights()
    draw_pieces()

    if is_checkmate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "CHECKMATE - "
            + get_bot_color().upper()
            + " WINS"
        )

    elif is_stalemate(
        chess_board,
        turn,
        en_passant_target
    ):

        game_over = True

        show_message(
            "STALEMATE"
        )

    elif in_check(
        chess_board,
        turn
    ):

        show_message(
            turn.upper()
            + " IS IN CHECK"
        )

    else:

        message_writer.clear()

    screen.update()

# bot connection fix

def bot_turn_after_player():

    if game_over:
        return

    if bot_is_turn():

        screen.ontimer(
            make_bot_move,
            500
        )


def fixed_board_click(x, y):

    if game_over:
        return

    old_turn = turn

    board_click(
        x,
        y
    )

    if (
        old_turn != turn
        and not game_over
        and bot_is_turn()
    ):

        screen.ontimer(
            make_bot_move,
            500
        )


def fixed_handle_click(x, y):

    if selected_difficulty is None:

        difficulty_click(
            x,
            y
        )

        return

    if selected_color is None:

        new_color_click(
            x,
            y
        )

        return

    fixed_board_click(
        x,
        y
    )

# iran mode optimized

IRAN_TIME_LIMIT = 3.0
iran_start_time = 0


def iran_time_up():

    return (
        time.time()
        - iran_start_time
        >= IRAN_TIME_LIMIT
    )


def iran_fast_evaluate(
    board,
    bot_color
):

    score = board_material_score(
        board,
        bot_color
    )

    enemy = other_color(
        bot_color
    )

    if in_check(
        board,
        bot_color
    ):

        score -= 150

    if in_check(
        board,
        enemy
    ):

        score += 150

    bot_moves = len(
        all_legal_moves(
            board,
            bot_color,
            None
        )
    )

    enemy_moves = len(
        all_legal_moves(
            board,
            enemy,
            None
        )
    )

    score += (
        bot_moves
        - enemy_moves
    ) * 4

    return score


def iran_search(
    board,
    color_to_move,
    bot_color,
    depth,
    alpha,
    beta
):

    if iran_time_up():

        return iran_fast_evaluate(
            board,
            bot_color
        )

    moves = all_legal_moves(
        board,
        color_to_move,
        None
    )

    if len(moves) == 0:

        if in_check(
            board,
            color_to_move
        ):

            if color_to_move == bot_color:

                return -10000000

            return 10000000

        return 0

    if depth <= 0:

        return iran_fast_evaluate(
            board,
            bot_color
        )

    moves = order_moves(
        board,
        moves
    )

    maximizing = (
        color_to_move == bot_color
    )

    if maximizing:

        best = -float("inf")

        for start, end in moves:

            if iran_time_up():
                break

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = iran_search(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score > best:
                best = score

            if score > alpha:
                alpha = score

            if beta <= alpha:
                break

        return best

    else:

        best = float("inf")

        for start, end in moves:

            if iran_time_up():
                break

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = iran_search(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score < best:
                best = score

            if score < beta:
                beta = score

            if beta <= alpha:
                break

        return best


def choose_iran_move():

    global iran_start_time

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:

        return None

    iran_start_time = time.time()

    bot_color = get_bot_color()

    best_move = moves[0]

    best_score = -float("inf")

    depth = 1

    while not iran_time_up():

        current_best = best_move
        current_score = -float("inf")

        ordered = order_moves(
            chess_board,
            moves
        )

        for start, end in ordered:

            if iran_time_up():
                break

            new_board = simulate_move(
                chess_board,
                start,
                end,
                en_passant_target
            )

            score = iran_search(
                new_board,
                other_color(turn),
                bot_color,
                depth - 1,
                -float("inf"),
                float("inf")
            )

            if score > current_score:

                current_score = score
                current_best = (
                    start,
                    end
                )

        if not iran_time_up():

            best_move = current_best
            best_score = current_score

        depth += 1

        if depth > 6:
            break

    return best_move


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    if selected_difficulty == "HARD":

        return choose_hard_move()

    if selected_difficulty == "INSANE":

        return choose_insane_move()

    if selected_difficulty == "IMPOSSIBLE":

        return choose_impossible_move()

    if selected_difficulty == "IRAN MODE":

        return choose_iran_move()

    return choose_random_move()

# impossible optimized

IMPOSSIBLE_TIME_LIMIT = 2.0
impossible_start_time = 0


def impossible_time_up():

    return (
        time.time()
        - impossible_start_time
        >= IMPOSSIBLE_TIME_LIMIT
    )


def impossible_fast_search(
    board,
    color_to_move,
    bot_color,
    depth,
    alpha,
    beta
):

    if impossible_time_up():

        return evaluate_board(
            board,
            bot_color
        )

    moves = all_legal_moves(
        board,
        color_to_move,
        None
    )

    if len(moves) == 0:

        if in_check(
            board,
            color_to_move
        ):

            if color_to_move == bot_color:

                return -10000000

            return 10000000

        return 0

    if depth <= 0:

        return evaluate_board(
            board,
            bot_color
        )

    moves = order_moves(
        board,
        moves
    )

    maximizing = (
        color_to_move == bot_color
    )

    if maximizing:

        best = -float("inf")

        for start, end in moves:

            if impossible_time_up():
                break

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = impossible_fast_search(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score > best:
                best = score

            if score > alpha:
                alpha = score

            if beta <= alpha:
                break

        return best

    else:

        best = float("inf")

        for start, end in moves:

            if impossible_time_up():
                break

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = impossible_fast_search(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score < best:
                best = score

            if score < beta:
                beta = score

            if beta <= alpha:
                break

        return best


def choose_impossible_move():

    global impossible_start_time

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:

        return None

    impossible_start_time = time.time()

    bot_color = get_bot_color()

    best_move = moves[0]

    depth = 1

    while not impossible_time_up():

        current_best = best_move
        current_score = -float("inf")

        ordered_moves = order_moves(
            chess_board,
            moves
        )

        for start, end in ordered_moves:

            if impossible_time_up():
                break

            new_board = simulate_move(
                chess_board,
                start,
                end,
                en_passant_target
            )

            score = impossible_fast_search(
                new_board,
                other_color(turn),
                bot_color,
                depth - 1,
                -float("inf"),
                float("inf")
            )

            if score > current_score:

                current_score = score

                current_best = (
                    start,
                    end
                )

        if not impossible_time_up():

            best_move = current_best

        depth += 1

        if depth > 6:
            break

    return best_move


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    if selected_difficulty == "HARD":

        return choose_hard_move()

    if selected_difficulty == "INSANE":

        return choose_insane_move()

    if selected_difficulty == "IMPOSSIBLE":

        return choose_impossible_move()

    if selected_difficulty == "IRAN MODE":

        return choose_iran_move()

    return choose_random_move()

# insane optimized

INSANE_TIME_LIMIT = 1.5
insane_start_time = 0


def insane_time_up():

    return (
        time.time()
        - insane_start_time
        >= INSANE_TIME_LIMIT
    )


def insane_fast_search(
    board,
    color_to_move,
    bot_color,
    depth,
    alpha,
    beta
):

    if insane_time_up():

        return evaluate_board(
            board,
            bot_color
        )

    moves = all_legal_moves(
        board,
        color_to_move,
        None
    )

    if len(moves) == 0:

        if in_check(
            board,
            color_to_move
        ):

            if color_to_move == bot_color:

                return -10000000

            return 10000000

        return 0

    if depth <= 0:

        return insane_evaluate(
            board,
            bot_color
        )

    moves = order_moves(
        board,
        moves
    )

    maximizing = (
        color_to_move == bot_color
    )

    if maximizing:

        best = -float("inf")

        for start, end in moves:

            if insane_time_up():
                break

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = insane_fast_search(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score > best:
                best = score

            if score > alpha:
                alpha = score

            if beta <= alpha:
                break

        return best

    else:

        best = float("inf")

        for start, end in moves:

            if insane_time_up():
                break

            new_board = simulate_move(
                board,
                start,
                end,
                None
            )

            score = insane_fast_search(
                new_board,
                other_color(
                    color_to_move
                ),
                bot_color,
                depth - 1,
                alpha,
                beta
            )

            if score < best:
                best = score

            if score < beta:
                beta = score

            if beta <= alpha:
                break

        return best


def choose_insane_move():

    global insane_start_time

    moves = all_legal_moves(
        chess_board,
        turn,
        en_passant_target
    )

    if len(moves) == 0:

        return None

    insane_start_time = time.time()

    bot_color = get_bot_color()

    best_move = moves[0]

    depth = 1

    while not insane_time_up():

        current_best = best_move
        current_score = -float("inf")

        ordered_moves = order_moves(
            chess_board,
            moves
        )

        for start, end in ordered_moves:

            if insane_time_up():
                break

            new_board = simulate_move(
                chess_board,
                start,
                end,
                en_passant_target
            )

            score = insane_fast_search(
                new_board,
                other_color(turn),
                bot_color,
                depth - 1,
                -float("inf"),
                float("inf")
            )

            if score > current_score:

                current_score = score

                current_best = (
                    start,
                    end
                )

        if not insane_time_up():

            best_move = current_best

        depth += 1

        if depth > 5:
            break

    return best_move


def choose_bot_move():

    if selected_difficulty == "EASY":

        return choose_random_move()

    if selected_difficulty == "MEDIUM":

        return choose_medium_move()

    if selected_difficulty == "HARD":

        return choose_hard_move()

    if selected_difficulty == "INSANE":

        return choose_insane_move()

    if selected_difficulty == "IMPOSSIBLE":

        return choose_impossible_move()

    if selected_difficulty == "IRAN MODE":

        return choose_iran_move()

    return choose_random_move()


# start

screen.onclick(
    fixed_handle_click
)

difficulty_screen()

screen.mainloop()