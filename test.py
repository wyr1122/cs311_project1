import time

from project1 import AI as AI1
from dev import AI as AI2
# from project1_templet import AI
import numpy as np


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


a = AI1(8, -1, 5)
b = AI2(8, 1, 5)
chessboard = np.array([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, -1, -1, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
cur = -1
skip = False
while (cur != 0):
    if cur == -1:
        nxt = a.go(chessboard)
    else:
        nxt = b.go(chessboard)
    if len(nxt) == 0:
        if skip:
            cnt1 = 0
            cnt2 = 0
            for i in range(8):
                for j in range(8):
                    if chessboard[i][j] == -1:
                        cnt1 += 1
                    if chessboard[i][j] == 1:
                        cnt2 += 1
            print(str(cnt1) + " : " + str(cnt2))
            break
        else:
            skip = True
    else:
        skip = False
        move(chessboard, nxt[-1][0], nxt[-1][1], cur)
    print(chessboard)
    cur = -cur
