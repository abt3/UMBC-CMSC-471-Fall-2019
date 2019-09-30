"""
Helper functions for the implementation of Minimax Algorithm to play Tic Tac Toe, using Python 3.
This software is available under GPL license.
Author: Fereydoon Vafaei    (a modified version of minimax algorithm in Russel's textbook,
                              and the code written by C. Cruz)
Year: 2019
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

def empty_cells(state):
    """
    Each empty cell will be added into cells list
    Args: state: the current state of the game board
    Return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y, board):
    """
    A move is valid if the chosen cell is empty
    Args x: X coordinate
         y: Y coordinate
         board: current board
    Return: True if the board cell at [x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player, board):
    """
    Set the move on board, if the coordinates are valid
    Args x: X coordinate
         y: Y coordinate
         player: the current player
         board: current board
    """
    if valid_move(x, y, board):
        board[x][y] = player
        return True
    else:
        return False
    
def print_board(state, ai_choice, human_choice):
    """
    Print the game board
    Args: state: current state of the board
          ai_choice, human_choice
    """

    chars = {
        +1: human_choice,
        -1: ai_choice,
        0: ' '
    }
    str_line = '=' * 15

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)        