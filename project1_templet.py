import numpy as np
import random
import time
from numba import jit
from functools import lru_cache

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
table = True
# block = True
color = 0
stable = 30
disk = 10
mobile = 80
final_depth = 11
cnt = 0
valueBoard = np.array([[-199, 48, -8, 6, 6, -8, 48, -199],
                       [48, -8, -16, 3, 3, -16, -8, 48],
                       [-8, -16, 4, 4, 4, 4, -16, -8],
                       [6, 1, 2, 0, 0, 2, 1, 6],
                       [6, 1, 2, 0, 0, 2, 1, 6],
                       [-8, -16, 4, 4, 4, 4, -16, -8],
                       [48, -8, -16, 3, 3, -16, -8, 48],
                       [-199, 48, -8, 6, 6, -8, 48, -199]])


# don't change the class name

class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
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
        global cnt, table, color, disk, stable, mobile
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
            Node.time = time.time()
            Node.depth = 2
            final = False
            if cnt <= final_depth:
                root = Node(0, -1, 0, -100000, 100000, -self.color, True, chessboard)
                root.final_search()
                print(root.alpha)
                if root.alpha >= 0:
                    self.candidate_list.append(root.step)
                    final = True
            # elif cnt <= 20:
            #     table = True
            #     stable = 40
            #     mobile = 100
            #     disk = 30
            # for i in range(8):
            #     if cnt - Node.depth <= 8:
            #         break
            #     root = Node(0, -1, 0, -100000, 100000, -self.color, True, chessboard)
            #     m = search(root)
            #     if m == 1:
            #         if i > 0:
            #             self.candidate_list.pop()
            #         self.candidate_list.append(root.step)
            #         print(Node.depth)
            #         print(root.step)
            #         print(time.time() - Node.time)
            #     Node.depth += 1
            # else:
            if not final:
                for i in range(8):
                    root = Node(0, -1, 0, -100000, 100000, -self.color, True, chessboard)
                    m = search(root)
                    if m == 1:
                        if i > 0:
                            self.candidate_list.pop()
                        self.candidate_list.append(root.step)
                        print(Node.depth)
                        print(root.step)
                        print(time.time() - Node.time)
                    Node.depth += 1
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


@jit(nopython=True)
def is_valid(color, x, y, chessboard):
    if chessboard[x][y] != COLOR_NONE:
        return False
    for i in range(8):
        for j in range(8):
            result = 1
            if chessboard[i][j] == color and (abs(x - i) > 1 or abs(y - j) > 1):
                if abs(x - i) == abs(y - j):
                    for k in range(abs(x - i) - 1):
                        k = k + 1
                        if chessboard[x + abs(i - x) // (i - x) * k][y + abs(j - y) // (j - y) * k] != -color:
                            result = 0
                    if result:
                        return True
                if i == x:
                    for k in range(abs(j - y) - 1):
                        k = k + 1
                        if chessboard[i][y + abs(j - y) // (j - y) * k] != -color:
                            result = 0
                    if result:
                        return True
                if j == y:
                    for k in range(abs(i - x) - 1):
                        k = k + 1
                        if chessboard[x + abs(i - x) // (i - x) * k][j] != -color:
                            result = 0
                    if result:
                        return True
    return False


@jit(nopython=True)
def get_value(chessboard, num):
    result = 0
    # if cnt > 18:
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
            elif is_valid(-color, i, j, chessboard):
                result -= mobile
    result += num * mobile
    # else:
    #     for i in range(8):
    #         for j in range(8):
    #             if chessboard[i][j] == color:
    #                 result += valueBoard[i][j]
    #                 result -= disk
    #             elif chessboard[i][j] == -color:
    #                 result += disk
    if cnt <= 20:
        for i in range(2):
            i = 7 * i
            for j in range(2):
                j = 7 * j
                if chessboard[i][j] == -color:
                    result += stable
                    for m in range(6):
                        if i == 7:
                            x = 6 - m
                        else:
                            x = m + 1
                        if chessboard[x][j] == -color:
                            result += stable
                            if m == 5 and i == 0:
                                if chessboard[7][j] == -color:
                                    result -= 6 * stable
                        else:
                            break
                    for m in range(6):
                        if j == 7:
                            y = 6 - m
                        else:
                            y = m + 1
                        if chessboard[i][y] == -color:
                            result += stable
                            if m == 5 and j == 0:
                                if chessboard[i][7] == -color:
                                    result -= 6 * stable
                        else:
                            break
    for i in range(2):
        i = 7 * i
        for j in range(2):
            j = 7 * j
            if chessboard[i][j] == color:
                result -= stable
                for m in range(6):
                    if i == 7:
                        x = 6 - m
                    else:
                        x = m + 1
                    if chessboard[x][j] == color:
                        result -= stable
                        if m == 5 and i == 0:
                            if chessboard[7][j] == color:
                                result += 6 * stable
                    else:
                        break
                for m in range(6):
                    if j == 7:
                        y = 6 - m
                    else:
                        y = m + 1
                    if chessboard[i][y] == color:
                        result -= stable
                        if m == 5 and j == 0:
                            if chessboard[i][7] == color:
                                result += 6 * stable
                    else:
                        break
    return result


@lru_cache()
def search(self):
    if self.ply == Node.depth:
        self.alpha = get_value(self.chessboard, len(self.parent.children))
        self.beta = self.alpha
        return
    for i in range(8):
        for j in range(8):
            if is_valid(-self.color, i, j, self.chessboard):
                child = Node(self, i, j, self.alpha, self.beta, -self.color, not self.is_max_node)
                self.children.append(child)
    if len(self.children) == 0:
        child = Node(self, -1, 0, self.alpha, self.beta, -self.color, not self.is_max_node)
        self.children.append(child)
    for child in self.children:
        # child.search()
        search(child)
        if self.is_max_node:
            if child.beta > self.alpha:
                self.alpha = child.beta
                if self.ply == 0:
                    self.step = child.step
            if self.alpha >= self.beta:
                self.alpha = self.beta
                return 1
        else:
            if child.alpha < self.beta:
                self.beta = child.alpha
            if self.alpha >= self.beta:
                self.beta = self.alpha
                return 1
        # if time.time() - Node.time > 5 - 0.14 * (Node.depth - 1):
        #     return 0
    return 1


# spec = [('valueBoard', int32[:]), ('time', int32), ('depth', int32), ('final_depth', int32), ('color', int32)]
# @jitclass(spec)
class Node(object):

    def __init__(self, parent, x, y, alpha, beta, color, is_max_node, chessboard=np.array([])):
        self.step = (x, y)
        self.alpha = alpha
        self.beta = beta
        self.parent = parent
        if parent != 0:
            self.chessboard = parent.chessboard.copy()
            self.ply = parent.ply + 1
        else:
            self.chessboard = chessboard.copy()
            self.ply = 0
        if x >= 0:
            self.chessboard[x][y] = color
            for i in range(8):
                for j in range(8):
                    result = 1
                    if self.chessboard[i][j] == color and (abs(x - i) > 1 or abs(y - j) > 1):
                        if abs(x - i) == abs(y - j):
                            for k in range(abs(x - i) - 1):
                                k = k + 1
                                if self.chessboard[x + abs(i - x) // (i - x) * k][
                                    y + abs(j - y) // (j - y) * k] != -color:
                                    result = 0
                            if result:
                                for k in range(abs(x - i) - 1):
                                    k = k + 1
                                    self.chessboard[x + abs(i - x) // (i - x) * k][
                                        y + abs(j - y) // (j - y) * k] = color

                        if i == x:
                            for k in range(abs(j - y) - 1):
                                k = k + 1
                                if self.chessboard[i][y + abs(j - y) // (j - y) * k] != -color:
                                    result = 0
                            if result:
                                for k in range(abs(j - y) - 1):
                                    k = k + 1
                                    self.chessboard[i][y + abs(j - y) // (j - y) * k] = color
                        if j == y:
                            for k in range(abs(i - x) - 1):
                                k = k + 1
                                if self.chessboard[x + abs(i - x) // (i - x) * k][j] != -color:
                                    result = 0
                            if result:
                                for k in range(abs(i - x) - 1):
                                    k = k + 1
                                    self.chessboard[x + abs(i - x) // (i - x) * k][j] = color
        self.color = color
        self.is_max_node = is_max_node
        self.children = []

    time = time.time()
    depth = 3

    @lru_cache()
    def final_search(self):
        final = True
        self_cnt = 0
        other_cnt = 0

        for i in range(8):
            for j in range(8):
                if self.chessboard[i][j] == color:
                    self_cnt += 1
                elif self.chessboard[i][j] == -color:
                    other_cnt += 1
                if is_valid(self.color, i, j, self.chessboard):
                    final = False
                if is_valid(-self.color, i, j, self.chessboard):
                    final = False
                    child = Node(self, i, j, self.alpha, self.beta, -self.color, not self.is_max_node)
                    self.children.append(child)
        if final:
            if self_cnt < other_cnt:
                result = 1
            elif self_cnt == other_cnt:
                result = 0
            else:
                result = -1
            self.alpha = result
            self.beta = result
            return
        if len(self.children) == 0:
            child = Node(self, -1, 0, self.alpha, self.beta, -self.color, not self.is_max_node)
            self.children.append(child)
        for child in self.children:
            child.final_search()
            if self.is_max_node:
                if child.beta > self.alpha:
                    self.alpha = child.beta
                    if self.ply == 0:
                        self.step = child.step
                if self.alpha >= self.beta:
                    self.alpha = self.beta
                    return 1
            else:
                if child.alpha < self.beta:
                    self.beta = child.alpha
                if self.alpha >= self.beta:
                    self.beta = self.alpha
                    return 1
            if time.time() - Node.time > 5 - 0.1 * cnt:
                return 0
        return 1
