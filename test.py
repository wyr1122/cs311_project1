import time

# from project1 import AI
from project1_templet import AI
import numpy as np

chess1 = np.array([[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, -1, -1, -1, 0, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, -1, -1, -1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, -1, -1, -1, 0, 0, 0], [0, 0, 1, -1, 1, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, -1, 0, 0, 0], [0, 0, 1, -1, 1, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, -1, -1, -1, -1, 0, 0, 0], [0, 0, -1, -1, 1, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, -1, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, 1, 0, 0, 0], [0, 0, 1, -1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, -1, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, -1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, -1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, -1, -1, -1, 0, 0, 0],
                    [0, -1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, -1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, -1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, -1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, -1, -1, 0, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
                    [0, 1, 1, 1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, -1, -1, 0, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, -1, -1, 0, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, -1, 1, 0, 0, 0, 0, 0], [0, -1, 1, 0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 0, 0, 0], [1, 0, 1, -1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0],
                    [0, -1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 1, 0, 0], [1, 0, 1, -1, 1, 0, 0, 0], [0, 0, 1, 1, -1, 0, 0, 0],
                    [0, -1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0, 0], [0, 0, 1, 0, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 1, 0, 0], [1, 0, 1, -1, 1, 0, 0, 0], [0, 0, 1, 1, -1, 0, 0, 0],
                    [0, -1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0, 0], [0, 0, 1, 0, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 1, 0, 0], [1, 0, 1, -1, 1, 0, 0, 0], [0, 0, 1, 1, -1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 1, 0, 0], [1, 0, 1, -1, 1, 0, 0, 0], [0, 0, 1, 1, -1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, 1, 0, 0], [1, 0, 1, -1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, -1, 0, 0], [1, 0, 1, -1, 1, 0, -1, 0], [0, 0, 1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, -1, 1, -1, -1, 0, 0], [1, 0, 1, 1, 1, 0, -1, 0], [0, 0, 1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, -1, 0, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, -1, 0, 0], [1, 0, -1, 1, 1, 0, -1, 0], [0, -1, 1, 1, 1, 1, 0, 0],
                    [1, -1, -1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, -1, 0, 0], [1, 0, -1, 1, 1, 0, -1, 0], [0, -1, 1, 1, 1, 1, 0, 0],
                    [1, -1, -1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, 0, -1, -1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, -1, 0, 0], [1, 0, -1, 1, 1, 0, -1, 0], [0, -1, 1, 1, 1, 1, 0, 0],
                    [1, -1, -1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, 0, -1, -1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, -1, 0, 0], [1, 1, 1, 1, 1, 0, -1, 0], [0, -1, 1, 1, 1, 1, 0, 0],
                    [1, -1, -1, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, 0, -1, -1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, -1, -1, 0, 0], [1, -1, 1, -1, 1, 0, -1, 0], [0, -1, -1, -1, 1, 1, 0, 0],
                    [1, -1, -1, -1, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, 1, -1, 0, 0], [1, -1, 1, -1, 1, 1, -1, 0], [0, -1, -1, -1, 1, 1, 0, 0],
                    [1, -1, -1, -1, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, 1, -1, -1, 0], [1, -1, 1, -1, 1, -1, -1, 0], [0, -1, -1, -1, -1, 1, 0, 0],
                    [1, -1, -1, -1, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, 1, -1, -1, 0], [1, -1, 1, -1, 1, -1, -1, 0], [0, -1, -1, -1, -1, 1, 0, 0],
                    [1, -1, -1, -1, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, -1, -1, 1, -1, -1, 0], [1, -1, 1, -1, 1, -1, -1, 0], [0, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, 1, -1, 1, -1, -1, 0], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, -1, 0, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, 0, -1, 1, -1, 0, 0, 0],
                    [-1, -1, 1, -1, 1, -1, -1, 0], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, -1, 0, 0, 0], [0, 0, 1, -1, 1, 0, 0, 0], [0, 0, -1, 1, 1, 1, 0, 0],
                    [-1, -1, 1, -1, 1, -1, -1, 0], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, -1, 0, 0, 0], [0, 0, 1, -1, 1, 0, 0, 0], [0, -1, -1, 1, 1, 1, 0, 0],
                    [-1, -1, -1, -1, 1, -1, -1, 0], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, -1, 0, 0, 0], [0, 0, 1, -1, 1, 0, 0, 0], [0, -1, -1, 1, 1, 1, 1, 0],
                    [-1, -1, -1, -1, 1, 1, -1, 0], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, -1, -1, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 1, 1, 1, 0],
                    [-1, -1, -1, -1, 1, 1, -1, 0], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 0, 1, -1, -1, 0, 0], [0, 0, 1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 1, 1, 1, 0],
                    [-1, -1, -1, -1, 1, 1, 1, 1], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, -1, -1, -1, -1, 0, 0], [0, 0, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 1, 1, 1, 0],
                    [-1, -1, -1, -1, 1, 1, 1, 1], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 1, 1, 1, 0],
                    [-1, -1, -1, -1, 1, 1, 1, 1], [1, 1, 1, -1, 1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, 0, -1], [0, -1, -1, -1, 1, 1, -1, 0],
                    [-1, -1, -1, -1, 1, -1, 1, 1], [1, 1, 1, -1, -1, -1, -1, 0], [1, -1, -1, -1, -1, -1, 0, 0],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, 0, -1], [0, -1, -1, -1, 1, 1, -1, 0],
                    [-1, -1, -1, -1, 1, 1, 1, 1], [1, 1, 1, -1, -1, -1, 1, 0], [1, -1, -1, -1, -1, -1, 0, 1],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, 0, -1], [0, -1, -1, -1, 1, 1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, -1, -1, 1, 0], [1, -1, -1, -1, -1, -1, 0, 1],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, 0, -1], [0, -1, -1, -1, 1, 1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, 1, 1], [1, 1, 1, -1, -1, -1, 1, 1], [1, -1, -1, -1, -1, -1, 0, 1],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, 0, -1], [0, -1, -1, -1, 1, 1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, -1, -1, -1, 1], [1, -1, -1, -1, -1, -1, -1, 1],
                    [1, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, 0, -1], [0, -1, -1, -1, 1, 1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, -1, 1, -1, 1], [1, -1, -1, -1, -1, -1, 1, 1],
                    [1, -1, -1, -1, -1, 0, 0, 1], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, -1, -1], [0, -1, -1, -1, 1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, 1, -1, 1], [1, 1, 1, -1, -1, 1, -1, 1], [1, -1, -1, -1, -1, -1, 1, 1],
                    [1, -1, -1, -1, -1, 0, 0, 1], [0, -1, -1, -1, 0, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, -1, -1], [0, -1, -1, -1, 1, -1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, 1, -1, 1, 1],
                    [1, -1, -1, 1, 1, 0, 0, 1], [0, -1, -1, -1, 1, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, -1, -1], [0, -1, -1, -1, 1, -1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, 1, -1, -1, 1],
                    [1, -1, -1, 1, 1, 0, -1, 1], [0, -1, -1, -1, 1, 0, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, -1, -1], [0, -1, -1, -1, 1, -1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, 1, -1, -1, 1],
                    [1, -1, -1, 1, 1, 0, 1, 1], [0, -1, -1, -1, 1, 1, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, -1, -1], [0, -1, -1, -1, 1, -1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, -1, -1, -1, -1, -1, 1, 1], [0, -1, -1, -1, 1, 1, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, 0, -1, -1], [0, -1, -1, -1, 1, -1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 0], [0, 0, -1, -1, -1, -1, -1, -1], [0, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 1], [0, 0, -1, -1, -1, -1, 1, 1], [0, -1, -1, -1, -1, 1, -1, 1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0]],
                   [[0, 1, 1, 1, 1, 1, 1, 1], [0, 0, -1, -1, -1, -1, 1, 1], [0, -1, -1, -1, -1, 1, -1, 1],
                    [-1, -1, -1, -1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, -1, 1], [1, 1, 1, 1, 1, 1, 0, -1]],
                   [[0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, -1, -1, 1, -1, 1],
                    [-1, 1, -1, 1, 1, 1, -1, 1], [1, 1, 1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, -1, 1], [1, 1, 1, 1, 1, 1, 0, -1]],
                   [[0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, 1, -1, 1],
                    [-1, -1, -1, 1, 1, 1, -1, 1], [1, 1, -1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, -1, 1], [1, 1, 1, 1, 1, 1, 0, -1]],
                   [[0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, 1],
                    [1, -1, -1, 1, 1, 1, -1, 1], [1, 1, -1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, -1, 1], [1, 1, 1, 1, 1, 1, 0, -1]],
                   [[-1, 1, 1, 1, 1, 1, 1, 1], [1, -1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, 1],
                    [1, -1, -1, 1, 1, 1, -1, 1], [1, 1, -1, -1, 1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, 1],
                    [1, 1, -1, -1, -1, -1, -1, 1], [1, 1, 1, 1, 1, 1, 0, -1]],
                   [[-1, 1, 1, 1, 1, 1, 1, 1], [1, -1, 1, 1, 1, 1, 1, 1], [1, 1, -1, -1, -1, 1, 1, 1],
                    [1, -1, 1, 1, 1, 1, 1, 1], [1, 1, -1, 1, 1, 1, 1, 1], [1, -1, 1, -1, 1, -1, 1, 1],
                    [1, 1, -1, -1, -1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, -1]]])
chess = np.array([[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, -1, -1, -1, 0, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, -1, -1, 1, 0, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, -1, -1, -1, -1, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0],
                   [0, 0, -1, -1, -1, 1, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0],
                   [0, 0, -1, -1, -1, 1, 0, 0], [0, 0, 0, -1, -1, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0],
                   [0, 0, -1, -1, -1, 1, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 1, -1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0],
                   [0, 0, -1, -1, -1, 1, 0, 0], [0, 0, 0, -1, -1, 0, 0, 0], [0, 0, 0, 1, -1, -1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, -1, 1, 0, 0], [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, 1, -1, -1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, -1, -1, -1, 0], [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, 1, -1, -1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, -1, -1, -1, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, -1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, 0, 0, 1, -1, 0, 1, 0],
                   [0, 0, -1, 1, -1, -1, -1, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, -1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, 0, 0, 1, -1, 0, 1, 0],
                   [0, 0, -1, 1, -1, -1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, -1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, -1], [0, 0, 0, 1, -1, 0, -1, 0],
                   [0, 0, -1, 1, -1, -1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, -1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 1, -1], [0, 0, 0, 1, -1, 0, 1, 0],
                   [0, 0, -1, 1, -1, -1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, -1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 1, -1], [0, 0, 0, 1, -1, 0, 1, 0],
                   [0, 0, -1, 1, -1, -1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, -1, -1, -1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 1, 0, 1, -1], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, 1, -1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, -1, -1, -1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 0, -1, -1, 0, 1, -1], [0, 0, 0, -1, 1, 0, 1, 0],
                   [0, 0, -1, 1, 1, -1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, -1, -1, -1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 1, -1, -1, 0, 1, -1], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, 1, -1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, -1, -1, -1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 1, -1, -1, 0, 1, -1], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, -1, -1, -1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 1, -1, -1, 0, 1, -1], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, -1, -1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 1, -1, -1, 0, 1, -1], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, -1, -1, 0],
                   [0, 0, 0, 0, 1, 0, -1, 0], [0, 0, 0, 0, 0, 0, -1, 0]],
                  [[0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 1, 1, 1, 1, 1, -1], [0, 0, 0, 1, 1, 0, 1, 0],
                   [0, 0, -1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, -1, -1, 0],
                   [0, 0, 0, 0, 1, 0, -1, 0], [0, 0, 0, 0, 0, 0, -1, 0]],
                  [[0, 0, 0, 0, 0, -1, -1, 0], [0, 0, 1, 1, 1, 1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0],
                   [0, 0, -1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, -1, -1, 0],
                   [0, 0, 0, 0, 1, 0, -1, 0], [0, 0, 0, 0, 0, 0, -1, 0]],
                  [[0, 0, 0, 0, 0, -1, -1, 0], [0, 0, 1, 1, 1, 1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0],
                   [0, 0, -1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, 1, -1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0],
                   [0, 0, -1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, 1, -1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 0, -1, 0],
                   [0, 0, 1, 1, 1, -1, -1, -1], [0, 1, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, 1, -1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 0, 1, -1, 1, -1, -1, -1], [0, 0, -1, 1, 1, 0, -1, 0],
                   [0, 0, 1, 1, 1, -1, -1, -1], [0, 1, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, 1, -1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, 1, 1, 0, -1, 0],
                   [0, 0, 1, 1, 1, -1, -1, -1], [0, 1, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, 1, -1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, 1, 1, 0, -1, 0],
                   [0, 0, 1, 1, 1, -1, -1, -1], [0, 1, 0, 1, 1, 0, -1, 0], [0, 0, 0, 1, 1, -1, -1, 0],
                   [0, 0, 0, 0, -1, 0, 1, 0], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, 1, 1, 0, -1, 0],
                   [0, 0, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, -1, 0, 1, 0], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, -1, 1, 0, -1, 0],
                   [0, 0, 1, -1, 1, 1, -1, -1], [0, 1, 0, -1, 1, 0, 1, 0], [0, 0, 0, -1, 1, 1, 1, 1],
                   [0, 0, 0, -1, -1, 0, 1, 0], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, -1, 1, 0, -1, 0],
                   [0, 0, 1, -1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, -1, -1, 0, 1, 0], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, -1, -1, -1, -1, 0],
                   [0, 0, 1, -1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, -1, -1, 0, 1, 0], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, -1, -1, 1, -1, 0],
                   [0, 0, 1, -1, 1, 1, 1, -1], [0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, -1, -1, 0, 1, 0], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 0], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, -1, -1, 1, -1, 0],
                   [0, 0, 1, -1, 1, 1, 1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [0, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, -1, -1, 0, 1, -1], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 1], [0, 1, 1, -1, 1, -1, 1, -1], [0, 0, 1, -1, -1, 1, -1, 0],
                   [0, 0, 1, -1, 1, 1, 1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [0, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, -1, -1, 0, 1, -1], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 0, 0, -1, -1, -1, 1], [0, 1, 1, -1, 1, -1, -1, -1], [0, 0, 1, -1, -1, 1, -1, -1],
                   [0, 0, 1, -1, 1, 1, 1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [0, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, -1, -1, 0, 1, -1], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, 0, -1, -1, -1, 1], [0, 1, 1, 1, 1, -1, -1, -1], [0, 0, 1, -1, 1, 1, -1, -1],
                   [0, 0, 1, -1, 1, 1, 1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [0, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, -1, -1, 0, 1, -1], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [0, 0, 1, -1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [0, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, -1, -1, 0, 1, -1], [0, 0, 0, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [0, 0, 1, -1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [0, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, 1, -1, 0, 1, -1], [0, 0, 1, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [0, 0, -1, -1, 1, 1, -1, -1], [0, -1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, 1, -1, 0, 1, -1], [0, 0, 1, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [0, 1, 1, 1, 1, 1, -1, -1], [0, -1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, 1, -1, 0, 1, -1], [0, 0, 1, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [0, 1, 1, 1, 1, 1, -1, -1], [0, -1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, 1, -1, 0, 1, -1], [0, -1, -1, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, 1, -1],
                   [0, 0, 0, 1, -1, 0, 1, -1], [0, -1, -1, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, -1, -1, -1, -1], [0, -1, -1, -1, 0, 0, -1, 1]],
                  [[0, 0, 1, -1, -1, -1, -1, 1], [0, 1, 1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[0, -1, -1, -1, -1, -1, -1, 1], [0, 1, -1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, -1, -1, -1, -1, -1, -1], [0, 0, 1, -1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, -1, -1, -1, -1, -1, -1], [0, -1, -1, -1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, -1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, 1, -1, 1, 1, -1, -1, -1],
                   [-1, -1, 1, 1, 1, 1, -1, -1], [-1, 1, 0, 1, 1, 0, 1, -1], [-1, 0, 1, 1, 1, 1, -1, -1],
                   [0, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, -1, -1, -1], [1, 1, -1, 1, 1, -1, -1, -1],
                   [1, -1, 1, 1, 1, 1, -1, -1], [1, 1, 0, 1, 1, 0, 1, -1], [1, 0, 1, 1, 1, 1, -1, -1],
                   [1, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, -1, -1, -1], [1, 1, -1, 1, -1, -1, -1, -1],
                   [1, -1, -1, -1, 1, 1, -1, -1], [1, 1, -1, 1, 1, 0, 1, -1], [1, 0, 1, 1, 1, 1, -1, -1],
                   [1, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, -1], [1, 1, -1, 1, 1, -1, -1, -1],
                   [1, -1, -1, 1, 1, 1, -1, -1], [1, 1, 1, 1, 1, 0, 1, -1], [1, 1, 1, 1, 1, 1, -1, -1],
                   [1, 0, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, -1], [1, 1, -1, 1, 1, -1, -1, -1],
                   [1, -1, -1, 1, -1, 1, -1, -1], [1, -1, 1, -1, 1, 0, 1, -1], [1, -1, -1, 1, 1, 1, -1, -1],
                   [1, -1, 0, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, -1], [1, 1, -1, 1, 1, -1, -1, -1],
                   [1, -1, -1, 1, -1, 1, -1, -1], [1, -1, 1, -1, 1, 0, 1, -1], [1, 1, 1, 1, 1, 1, -1, -1],
                   [1, 1, 1, 1, 1, 1, -1, -1], [0, -1, -1, -1, 0, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, -1], [1, 1, -1, 1, 1, -1, -1, -1],
                   [1, -1, -1, 1, -1, 1, -1, -1], [1, -1, 1, -1, -1, 0, 1, -1], [1, 1, -1, 1, -1, 1, -1, -1],
                   [1, 1, 1, -1, -1, -1, -1, -1], [0, -1, -1, -1, -1, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, -1], [1, 1, -1, 1, 1, -1, -1, -1],
                   [1, -1, -1, 1, -1, 1, -1, -1], [1, -1, 1, -1, -1, 0, 1, -1], [1, 1, -1, 1, -1, 1, -1, -1],
                   [1, 1, 1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1, 1, 1]],
                  [[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, -1, -1], [1, 1, -1, 1, 1, -1, -1, -1],
                   [1, -1, -1, 1, -1, -1, -1, -1], [1, -1, 1, -1, -1, -1, -1, -1], [1, 1, -1, 1, -1, -1, -1, -1],
                   [1, 1, 1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1, 1, 1]]])
ai = AI(8, -1, 5)
chessboard = chess[29]
print(chessboard)
start = time.time()
ai.go(chessboard)
print(time.time() - start)
