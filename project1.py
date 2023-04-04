import numpy as np
import random
import time
from numba import njit, objmode

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)

# args
table = False
final_table = True
stable = 100
disk = 50
mobile = 100
final_mobile = 200
final_stable = 60
final_disk = 30
mid_depth = 36
final_depth = 14
final_search_depth = 8

valueBoard = np.array([[-99, 48, -8, 6, 6, -8, 48, -99],
                       [48, -8, -16, 3, 3, -16, -8, 48],
                       [-8, -16, 4, 4, 4, 4, -16, -8],
                       [6, 1, 2, 0, 0, 2, 1, 6],
                       [6, 1, 2, 0, 0, 2, 1, 6],
                       [-8, -16, 4, 4, 4, 4, -16, -8],
                       [48, -8, -16, 3, 3, -16, -8, 48],
                       [-99, 48, -8, 6, 6, -8, 48, -99]])

# final_valueBoard = np.loadtxt('board.txt')


final_valueBoard = np.array([[-199, 88, -8, 6, 6, -8, 88, -199],
                             [88, -8, -16, 3, 3, -16, -8, 88],
                             [-8, -16, 4, 4, 4, 4, -16, -8],
                             [6, 1, 2, 0, 0, 2, 1, 6],
                             [6, 1, 2, 0, 0, 2, 1, 6],
                             [-8, -16, 4, 4, 4, 4, -16, -8],
                             [88, -8, -16, 3, 3, -16, -8, 88],
                             [-199, 88, -8, 6, 6, -8, 88, -199]])


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
        start = time.time()
        color = -1
        final_search(
            np.array([[-1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, 1, -1, 1, 1], [-1, 1, 1, 1, -1, 1, -1, 1],
                      [-1, 1, 1, -1, 1, -1, 1, 1], [-1, 1, 1, -1, -1, 1, -1, 1], [-1, -1, -1, -1, -1, -1, 1, 1],
                      [-1, -1, 1, 1, 1, 1, 1, 1], [-1, 1, 1, 1, 1, 1, 0, 0]]), -color, 0, True, start,
            color, 2)

        # The input is the current chessboard. Chessboard is a numpy array.

    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        # ==================================================================
        # Write your algorithm here
        global disk, stable, mobile
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
            depth = 4
            final = False
            if cnt <= final_depth:
                v, step = final_search(chessboard, -color, 0, True, start, color, cnt)
                print(v)
                print(time.time() - start)
                if step[0] >= 0:
                    if v >= 0 or cnt > final_search_depth:
                        print(step)
                        self.candidate_list.append(step)
                        final = True
            if not final:
                for i in range(10):
                    print(depth)
                    v, step = search(chessboard, -color, -10000, 10000, 0, True, 0, depth, start, color, cnt)
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


@njit()
def search(chessboard, c, alpha, beta, ply, is_max_node, num, depth, start, color, cnt):
    if ply == depth:
        return get_value(chessboard, num, color, cnt, c), (-1, 0)
    moves = get_moves(chessboard, -c)
    step = (-1, 0)
    if len(moves) == 0:
        moves.append([-1, 0])
    for x, y in moves:
        v, _ = search(move(chessboard, x, y, -c), -c, alpha, beta, ply + 1, not is_max_node, len(moves), depth, start,
                      color, cnt)
        if is_max_node:
            if v > alpha:
                alpha = v
                step = (x, y)
            if alpha >= beta:
                return beta, step
        else:
            if v < beta:
                beta = v
                step = (x, y)
            if alpha >= beta:
                return alpha, step
        with objmode(t='f8'):
            t = time.time()
        if t - start > 4.99:
            return 0, (-1, 0)
        # if ply == 0:
        #     print(x, y, v, step)
    if is_max_node:
        return alpha, step
    else:
        return beta, step


@njit()
def final_search(chessboard, c, ply, is_max_node, start, color, cnt):
    final = True
    self_cnt = 0
    other_cnt = 0
    moves = get_moves(chessboard, -c)
    step = (-1, 0)
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
    if final:
        if self_cnt < other_cnt:
            result = 1
        elif self_cnt == other_cnt:
            result = 0
        else:
            result = -1
        return result, (-1, 0)
    if len(moves) == 0:
        moves.append([-1, 0])
    if is_max_node:
        value = -2
    elif cnt <= final_search_depth:
        value = 2
    else:
        value = 0
    for x, y in moves:
        v, _ = final_search(move(chessboard, x, y, -c), -c, ply + 1, not is_max_node, start, color,
                            cnt)
        # if ply == 0:
        #     print(x, y, v)
        if is_max_node:
            if v > value:
                value = v
                step = (x, y)
            if value == 1:
                return value, step
        elif cnt <= final_search_depth:
            if v < value:
                value = v
                step = (x, y)
            if value == -1:
                return value, step
        else:
            value += v / len(moves)
            step = (x, y)
        with objmode(t='f8'):
            t = time.time()
        if t - start > 4:
            return -111, (-1, 0)
    return value, step


@njit()
def get_value(chessboard, num, color, cnt, c):
    result = 0
    if cnt > mid_depth:
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == color:
                    if table:
                        result += valueBoard[i][j]
                    result -= disk
                elif chessboard[i][j] == -color:
                    if table:
                        result -= valueBoard[i][j]
                    result += disk
                elif is_valid(-c, i, j, chessboard):
                    result -= color * c * mobile
        result += num * color * c * mobile
        result -= get_stable(chessboard, color) * stable
    else:
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == color:
                    if final_table:
                        result += final_valueBoard[i][j]
                    result -= final_disk
                elif chessboard[i][j] == -color:
                    if final_table:
                        result -= final_valueBoard[i][j]
                    result += final_disk
                elif is_valid(-c, i, j, chessboard):
                    result -= color * c * (final_mobile - (cnt - 8) * 5)
        if (color == c and cnt % 2 == 0) or (color != c and cnt % 2 != 0):
            result -= 200
        result += num * color * c * (final_mobile - (cnt - 8) * 5)
        result += get_stable(chessboard, -color) * final_stable
        result -= get_stable(chessboard, color) * final_stable
    return result


@njit()
def get_moves(chessboard, c):
    moves = []
    for i in range(8):
        for j in range(8):
            if is_valid(c, i, j, chessboard):
                moves.append([i, j])
    return moves


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
