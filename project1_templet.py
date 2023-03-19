import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)


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
        root = Node(0, -1, 0, -100000, 100000, -self.color, True, chessboard)
        cnt = 0
        Node.color = self.color
        for x in range(8):
            for y in range(8):
                if chessboard[x][y] == COLOR_NONE:
                    cnt += 1
                if is_valid(self.color, x, y, chessboard):
                    self.candidate_list.append((x, y))
        # print(root.get_value())
        if len(self.candidate_list) != 0:
            Node.time = time.time()
            Node.depth = 3
            if cnt <= Node.final_depth:
                root.final_search()
                print(root.alpha)
                self.candidate_list.append(root.step)
            else:
                for i in range(3):
                    m = root.search()
                    if m == 1:
                        if i > 0:
                            self.candidate_list.pop()
                        self.candidate_list.append(root.step)
                        print(Node.depth)
                    Node.depth += 1

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


class Node(object):
    valueBoard = [[-99, 48, -8, 6, 6, -8, 48, -99],
                  [48, -8, -16, 3, 3, -16, -8, 48],
                  [-8, -16, 4, 4, 4, 4, -16, -8],
                  [6, 1, 2, 0, 0, 2, 1, 6],
                  [6, 1, 2, 0, 0, 2, 1, 6],
                  [-8, -16, 4, 4, 4, 4, -16, -8],
                  [48, -8, -16, 3, 3, -16, -8, 48],
                  [-99, 48, -8, 6, 6, -8, 48, -99]]
    time = time.time()
    depth = 3
    final_depth = 8
    color = 0

    def __init__(self, parent, x, y, alpha, beta, color, is_max_node, chessboard=[]):
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
        self.color = color
        self.is_max_node = is_max_node
        self.children = []

    def search(self):
        if self.ply == Node.depth:
            self.alpha = self.get_value()
            self.beta = self.get_value()
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
            child.search()
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
            if time.time() - Node.time > 4.95:
                return 0
        return 1

    def final_search(self):
        final = True
        self_cnt = 0
        other_cnt = 0

        for i in range(8):
            for j in range(8):
                if self.chessboard[i][j] == Node.color:
                    self_cnt += 1
                elif self.chessboard[i][j] == -Node.color:
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
            # if time.time() - Node.time > 4.95:
            #     return 0
        return 1

    def get_value(self):
        result = 0
        for i in range(8):
            for j in range(8):
                if self.chessboard[i][j] == Node.color:
                    result += Node.valueBoard[i][j]
                    result -= 5
                if self.chessboard[i][j] == -Node.color:
                    result += 5
                elif is_valid(-Node.color, i, j, self.chessboard):
                    result -= 20
        result += len(self.parent.children) * 20
        for i in range(2):
            i = 7 * i
            for j in range(2):
                j = 7 * j
                if self.chessboard[i][j] == Node.color:
                    result -= 15
                    for m in range(6):
                        if i == 7:
                            x = 6 - m
                        else:
                            x = m + 1
                        if self.chessboard[x][j] == Node.color:
                            result -= 15
                            if m == 5 and i == 0:
                                if self.chessboard[7][j] == Node.color:
                                    result += 90
                        else:
                            break
                    for m in range(6):
                        if j == 7:
                            y = 6 - m
                        else:
                            y = m + 1
                        if self.chessboard[i][y] == Node.color:
                            result -= 20
                            if m == 5 and j == 0:
                                if self.chessboard[i][7] == Node.color:
                                    result += 120
                        else:
                            break
        return result
