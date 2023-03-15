from project1_templet import AI
import numpy as np

ai = AI(8, -1, 5)
chessboard = np.array(
    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, -1, -1, -1, 1, -1, -1], [0, 0, -1, -1, 1, 1, -1, 0],
     [0, 1, 1, 1, 1, 1, -1, 0], [0, 0, -1, -1, -1, -1, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
ai.go(chessboard)
ai.go(chessboard)
