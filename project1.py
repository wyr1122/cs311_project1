import numpy as np
import random
import time
from numba import njit, objmode
from functools import lru_cache, wraps

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
color = 0
cnt = 0
start = 0
depth = 0

# args
table = True
stable = 30
disk = 50
mobile = 80
final_mobile = 20
final_stable = 50
final_depth = 12
heuristic_cutoffs_depth = 3

valueBoard = np.array([[-399, 88, -8, 6, 6, -8, 88, -399],
                       [88, -8, -16, 3, 3, -16, -8, 88],
                       [-8, -16, 4, 4, 4, 4, -16, -8],
                       [6, 1, 2, 0, 0, 2, 1, 6],
                       [6, 1, 2, 0, 0, 2, 1, 6],
                       [-8, -16, 4, 4, 4, 4, -16, -8],
                       [88, -8, -16, 3, 3, -16, -8, 88],
                       [-399, 88, -8, 6, 6, -8, 88, -399]])


# don't change the class name

class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, c, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = c
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need to add your decision to your candidate_list. The system will get the end of your candidate_list as
        # your decision.
        self.candidate_list = []

    # The input is the current chessboard. Chessboard is a numpy array.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        # ==================================================================
        # Write your algorithm here
        global cnt, table, color, disk, stable, mobile, start, depth
        cnt = 0
        color = self.color
        for x in range(8):
            for y in range(8):
                if chessboard[x][y] == COLOR_NONE:
                    cnt += 1
                if is_valid(self.color, x, y, chessboard):
                    self.candidate_list.append((x, y))
        # print(root.get_value())
        if len(self.candidate_list) != 0:
            start = time.time()
            depth = 2
            final = False
            if cnt <= final_depth:
                v, step = final_search(chessboard, -color, -10000, 10000, 0, True)
                print(v)
                print(time.time() - start)
                if step[0] >= 0:
                    if v >= 0:
                        print(step)
                        self.candidate_list.append(step)
                        final = True
            if not final:
                for i in range(10):
                    v, step = search(chessboard, -color, -10000, 10000, 0, True, 0)
                    print(depth)
                    if step[0] >= 0:
                        if i > 0:
                            self.candidate_list.pop()
                        self.candidate_list.append(step)
                        print(v)
                        print(step)
                    print(time.time() - start)
                    depth += 1
            print(self.candidate_list)
            # Here is the simplest sample:Random decision
    # idx = np.where(chessboard == COLOR_NONE)
    # idx = list(zip(idx[0], idx[1]))
    # ==============Find new pos========================================
    # Make sure that the position of your decision on the chess board is empty.
    # If not, the system will return error.
    # Add your decision into candidate_list, Records the chessboard
    # You need to add all the positions which are valid
    # candidate_list example: [(3,3),(4,4)]
    # You need append your decision at the end of the candidate_list,
    # candidate_list example: [(3,3),(4,4),(4,4)]
    # we will pick the last element of the candidate_list as the position you choose.
    # In above example, we will pick (4,4) as your decision.
    # If there is no valid position, you must return an empty


# def np_cache(function):
#     @lru_cache()
#     def cached_wrapper(hashable_array, c, alpha, beta, ply, is_max_node, num):
#         array = np.array(hashable_array)
#         return function(array, c, alpha, beta, ply, is_max_node, num)
#
#     @wraps(function)
#     def wrapper(array, c, alpha, beta, ply, is_max_node, num):
#         return cached_wrapper(tuple(array), c, alpha, beta, ply, is_max_node, num)
#
#     # copy lru_cache attributes over too
#     wrapper.cache_info = cached_wrapper.cache_info
#     wrapper.cache_clear = cached_wrapper.cache_clear
#
#     return wrapper


# @lru_cache()
def search(chessboard, c, alpha, beta, ply, is_max_node, num):
    if ply == depth:
        return get_value(chessboard, num), [-1, 0]
    moves = get_moves(chessboard, -c, num, ply < heuristic_cutoffs_depth)
    step = [-1, 0]
    if len(moves) == 0:
        moves.append([0, -1, 0])
    if ply < heuristic_cutoffs_depth:
        moves.sort(reverse=True)
    for _, x, y in moves:
        v, _ = search(move(chessboard, x, y, -c), -c, alpha, beta, ply + 1, not is_max_node, len(moves))
        if is_max_node:
            if v > alpha:
                alpha = v
                step = [x, y]
            if alpha >= beta:
                return beta, step
        else:
            if v < beta:
                beta = v
                step = [x, y]
            if alpha >= beta:
                return alpha, step
        t = time.time()
        # with objmode(t='int32'):
        #     t = time.time()
        # if t - start > 5 - 0.15 * (depth - 3):
        if t - start > 4:
            return 0, [-1, 0]
    if is_max_node:
        return alpha, step
    else:
        return beta, step


def final_search(chessboard, c, alpha, beta, ply, is_max_node):
    final = True
    self_cnt = 0
    other_cnt = 0
    step = [-1, 0]
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == color:
                self_cnt += 1
            elif chessboard[i][j] == -color:
                other_cnt += 1
            if is_valid(c, i, j, chessboard):
                final = False
            if is_valid(-c, i, j, chessboard):
                final = False
                # child = Node(self, i, j, self.alpha, self.beta, -self.color, not self.is_max_node)
                # self.children.append(child)
    if final:
        if self_cnt < other_cnt:
            result = 1
        elif self_cnt == other_cnt:
            result = 0
        else:
            result = -1
        return result, [-1, 0]
    moves = get_moves(chessboard, -c, 0, False)
    if len(moves) == 0:
        moves.append([-1, 0, 0])
    for _, x, y in moves:
        v, _ = final_search(move(chessboard, x, y, -c), -c, alpha, beta, ply + 1, not is_max_node)
        if is_max_node:
            if v > alpha:
                alpha = v
                step = [x, y]
            if alpha >= beta:
                return beta, step
        else:
            if v < beta:
                beta = v
                step = [x, y]
            if alpha >= beta:
                return alpha, step
        # if time.time() - start > 5 - 0.08 * cnt:
        if time.time() - start > 3.5:
            return -111, [-1, 0]
    if is_max_node:
        return alpha, step
    else:
        return beta, step


@njit()
def is_valid(c, x, y, chessboard):
    if chessboard[x][y] != COLOR_NONE:
        return False
    for i in range(8):
        for j in range(8):
            result = 1
            if chessboard[i][j] == c and (abs(x - i) > 1 or abs(y - j) > 1):
                if abs(x - i) == abs(y - j):
                    for k in range(abs(x - i) - 1):
                        k = k + 1
                        if chessboard[x + abs(i - x) // (i - x) * k][y + abs(j - y) // (j - y) * k] != -c:
                            result = 0
                    if result:
                        return True
                if i == x:
                    for k in range(abs(j - y) - 1):
                        k = k + 1
                        if chessboard[i][y + abs(j - y) // (j - y) * k] != -c:
                            result = 0
                    if result:
                        return True
                if j == y:
                    for k in range(abs(i - x) - 1):
                        k = k + 1
                        if chessboard[x + abs(i - x) // (i - x) * k][j] != -c:
                            result = 0
                    if result:
                        return True
    return False


@njit()
def get_moves(chessboard, c, num, evaluation):
    moves = []
    for i in range(8):
        for j in range(8):
            if is_valid(c, i, j, chessboard):
                new_cb = move(chessboard, i, j, c)
                if evaluation:
                    moves.append([c * color * get_value(new_cb, num), i, j])
                else:
                    moves.append([0, i, j])
    return moves


@njit()
def get_value(chessboard, num):
    result = 0
    if cnt > 30:
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == color:
                    # if table:
                    #     result += valueBoard[i][j]
                    result -= disk
                elif chessboard[i][j] == -color:
                    # if table:
                    #     result -= valueBoard[i][j]
                    result += disk
                elif is_valid(-color, i, j, chessboard):
                    result -= mobile
        result += num * mobile
        result -= get_stable(chessboard, color) * stable
    else:
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == color:
                    if table:
                        result += valueBoard[i][j]
                elif chessboard[i][j] == -color:
                    if table:
                        result -= valueBoard[i][j]
                # elif is_valid(-color, i, j, chessboard):
                #     result -= final_mobile
        result += num * final_mobile
        result += get_stable(chessboard, -color) * final_stable
        result -= get_stable(chessboard, color) * final_stable
    return result


@njit()
def get_stable(chessboard, c):
    result = 0
    stable_board = [[0] * 8 for _ in range(8)]
    for i in range(2):
        i = 7 * i
        for j in range(2):
            j = 7 * j
            if chessboard[i][j] == c:
                stable_board[i][j] = 1
                for m in range(6):
                    if i == 7:
                        x = 6 - m
                    else:
                        x = m + 1
                    if chessboard[x][j] == c:
                        stable_board[x][j] = 1
                    else:
                        break
                for m in range(6):
                    if j == 7:
                        y = 6 - m
                    else:
                        y = m + 1
                    if chessboard[i][y] == c:
                        stable_board[i][y] = 1
                    else:
                        break
    directions = [(1, 0), (1, 1), (-1, 1), (0, 1)]
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == c:
                stb = True
                for direction in directions:
                    stb_line = True
                    x = i
                    y = j
                    while 0 <= x < 8 and 0 <= y < 8:
                        if chessboard[x][y] == 0:
                            stb_line = False
                            break
                        x += direction[0]
                        y += direction[1]
                    x = i
                    y = j
                    while 0 <= x < 8 and 0 <= y < 8:
                        if chessboard[x][y] == 0:
                            stb_line = False
                            break
                        x -= direction[0]
                        y -= direction[1]
                    x = i
                    y = j
                    stb_fix = True
                    while 0 <= x < 8 and 0 <= y < 8:
                        if chessboard[x][y] != c:
                            stb_fix = False
                            break
                        x += direction[0]
                        y += direction[1]
                    if stb_fix:
                        stb_line = True
                    x = i
                    y = j
                    stb_fix = True
                    while 0 <= x < 8 and 0 <= y < 8:
                        if chessboard[x][y] != c:
                            stb_fix = False
                            break
                        x -= direction[0]
                        y -= direction[1]
                    if stb_fix:
                        stb_line = True
                    if not stb_line:
                        stb = False
                if stb:
                    stable_board[i][j] = 1
    for i in range(8):
        for j in range(8):
            if stable_board[i][j] == 1:
                result += 1
    return result


@njit()
def move(cb, x, y, color):
    chessboard = cb.copy()
    if x >= 0:
        chessboard[x][y] = color
        for i in range(8):
            for j in range(8):
                result = 1
                if chessboard[i][j] == color and (abs(x - i) > 1 or abs(y - j) > 1):
                    if abs(x - i) == abs(y - j):
                        for k in range(abs(x - i) - 1):
                            k = k + 1
                            if chessboard[x + abs(i - x) // (i - x) * k][
                                y + abs(j - y) // (j - y) * k] != -color:
                                result = 0
                        if result:
                            for k in range(abs(x - i) - 1):
                                k = k + 1
                                chessboard[x + abs(i - x) // (i - x) * k][
                                    y + abs(j - y) // (j - y) * k] = color

                    if i == x:
                        for k in range(abs(j - y) - 1):
                            k = k + 1
                            if chessboard[i][y + abs(j - y) // (j - y) * k] != -color:
                                result = 0
                        if result:
                            for k in range(abs(j - y) - 1):
                                k = k + 1
                                chessboard[i][y + abs(j - y) // (j - y) * k] = color
                    if j == y:
                        for k in range(abs(i - x) - 1):
                            k = k + 1
                            if chessboard[x + abs(i - x) // (i - x) * k][j] != -color:
                                result = 0
                        if result:
                            for k in range(abs(i - x) - 1):
                                k = k + 1
                                chessboard[x + abs(i - x) // (i - x) * k][j] = color
    return chessboard

    # spec = [('valueBoard', int32[:]), ('time', int32), ('depth', int32), ('final_depth', int32), ('color', int32)]
    # @jitclass(spec)
    # class Node(object):
