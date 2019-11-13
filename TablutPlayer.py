import numpy as np

minus_inf = -2
plus_inf = 2
max_depth = 3

def eval_function(state):

def alpha_beta_search(state):
    moves = state.get_all_legal_moves()
    movesValue = np.array(size(moves))
    moveIndex = 0
    for move in moves:
        next_state = state.next_state_with_move(move)
        movesValue[moveIndex] = max_value(next_state, minus_inf, plus_inf, 1)
        moveIndex += 1
    best_move_index = np.where(movesValue == max(movesValue))
    best_move = moves(best_move_index)
    return best_move

def max_value(state, alpha, beta, depth):
    if state.game_over():
        return eval_function(state)
    if depth == max_depth:
        return eval_function(state)
    v = minus_inf
    moves = state.get_all_legal_moves()
    for move in moves:
        next_state = state.next_state_with_move(move)
        v = max(v, min_value(next_state, alpha, beta, depth+1))
        if v >= beta:
            return v
        alpha = min(alpha, v)
    return v

def min_value(state, alpha, beta):
    if state.game_over():
        return eval_function(state)
    if depth == max_depth:
        return eval_function(state)
    v = plus_inf
    moves = state.get_all_legal_moves()
    for move in moves:
        next_state = state.next_state_with_move(move)
        v = min(v, max_value(next_state, alpha, beta, depth+1))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

class TablutPlayer:
    def __init__(state, team):
        self.state = state
        self.team = team

