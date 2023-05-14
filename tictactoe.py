"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for col in row:
            if col == None:
                count += 1

    if count == 9:
        return X
    elif count % 2 == 0:
        return O
    elif count % 2 == 1:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)

    if board[action[0]][action[1]] != EMPTY:
        raise ValueError

    copy_board = copy.deepcopy(board)
    copy_board[action[0]][action[1]] = player_turn

    return copy_board


def check_row(board, player):
    """
    check for all three rows
    """
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    return False


def check_col(board, player):
    """
    check for all three columns
    """
    for row in board:
        for i, col in enumerate(row):
            if col == player and board[1][i] == player and board[2][i] == player:
                return True
        return False


def check_dig(board, player):
    """
    check for both diagonal 
    """
    for row in board:
        for col in row:
            if col == player and board[1][1] == player and board[2][2] == player:
                return True
            if row[2] == player and board[1][1] == player and board[2][0] == player:
                return True
            return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if check_col(board, X) or check_dig(board, X) or check_row(board, X):
        return X
    if check_col(board, O) or check_dig(board, O) or check_row(board, O):
        return O
    if len(actions(board)) != 0:
        return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if len(actions(board)) > 0:
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        return 0

    player = winner(board)
    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_turn = player(board)

    actionsStart = actions(board)
    
    if len(actionsStart) == 9:
        return random.choice(list(actionsStart))

    moves = list()

    for action in actions(board):
        if player_turn == X:
            value = min_value(result(board, action))
            moves.append((value, action))
        elif player_turn == O:
            value = max_value(result(board, action))
            moves.append((value, action))

    # if len(l)== 9:
    #     return random.random(moves)[1]

    if player_turn == X:
        moves.sort(reverse=True)
        return moves[0][1]
    elif player_turn == O:
        moves.sort()
        return moves[0][1]
