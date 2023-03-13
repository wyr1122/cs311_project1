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

        for x in range(8):
            for y in range(8):
                if self.is_valid(x, y, chessboard):
                    self.candidate_list.append((x, y))
        if len(self.candidate_list) != 0:
            self.candidate_list.append(self.candidate_list[0])

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

    def is_valid(self, x, y, chessboard):
        if chessboard[x][y] != COLOR_NONE:
            return False
        for i in range(8):
            for j in range(8):
                result = 1
                if chessboard[i][j] == self.color and (abs(x - i) > 1 or abs(y - j) > 1):
                    if abs(x - i) == abs(y - j):
                        for k in range(abs(x - i) - 1):
                            k = k + 1
                            if chessboard[x + abs(i - x) // (i - x) * k][y + abs(j - y) // (j - y) * k] != -self.color:
                                result = 0
                        if result:
                            return True
                    if i == x:
                        for k in range(abs(j - y) - 1):
                            k = k + 1
                            if chessboard[i][y + abs(j - y) // (j - y) * k] != -self.color:
                                result = 0
                        if result:
                            return True
                    if j == y:
                        for k in range(abs(i - x) - 1):
                            k = k + 1
                            if chessboard[x + abs(i - x) // (i - x) * k][j] != -self.color:
                                result = 0
                            if result:
                                return True
        return False
