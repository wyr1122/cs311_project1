import time

from project1_templet import AI
import numpy as np

ai = AI(8, -1, 5)
chessboard = np.array(
    [[0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 1, 0, 1, 1, 1, 1], [-1, -1, 1, 1, 1, 1, 1, 1], [-1, 1, 1, -1, 1, 1, 1, 1],
     [0, 0, 1, -1, 1, 1, 1, 0], [-1, 1, 0, 0, 0, 1, 1, 1], [-1, -1, 1, 1, 0, 0, 1, 1], [-1, 0, 0, 1, 0, 1, 1, 1]])
start = time.time()
ai.go(chessboard)
print(time.time() - start)
# ai.go(chessboard)
