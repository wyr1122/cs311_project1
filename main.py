from project1_templet import AI
import numpy as np

ai = AI(8, -1, 5)
chessboard = np.zeros((8, 8))
chessboard[3][5] = -1
chessboard[4][4] = 1
chessboard[5][3] = 1
ai.go(chessboard)
