import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def is_valif_location(board, column):
    return board[5][column] == 0


def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))


board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        column = int(input("Player 1 Make your Selection (0-6):"))

        if is_valif_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

    # Ask for Player 2 Input
    else:
        column = int(input("Player 2 Make your Selection (0-6):"))

        if is_valif_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)
    
    print_board(board)

    turn += 1  
    turn = turn % 2
