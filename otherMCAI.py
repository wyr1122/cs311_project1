import copy

import numpy as np
import random
import time

from numba import jit

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
COLOR = 0
n = 0
last = 0


class Node:
    def __init__(self, g, color, fa):
        self.g = copy.deepcopy(g)
        self.n = 0
        self.w = 0
        self.color = color
        self.fa = fa
        self.sons = []


random.seed(0)
root = Node(None, None, None)
round_count = 0


@jit(nopython=True)
def is_out(x, y, n):
    if x < 0 or x >= n or y < 0 or y >= n: return True
    return False


class AI(object):
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        self.color = color
        self.time_out = time_out
        self.candidate_list = []
        global n, COLOR
        n = chessboard_size
        COLOR = color

    def go(self, chessboard):
        global n, last
        self.candidate_list.clear()
        self.candidate_list = get_candidate_list(chessboard, COLOR)

        last = int(0)
        for i in range(n):
            for j in range(n):
                if chessboard[i][j] == COLOR_NONE: last += 1

        res = (-1, -1)
        if last < 13:
            for x, y in self.candidate_list:
                cur_g = nxt(copy.deepcopy(chessboard), x, y, COLOR)
                if dfs(-COLOR, cur_g) == -1:
                    res = (x, y)
                    break
                elif dfs(-COLOR, cur_g) == 0:
                    res = (x, y)

        if res[0] == -1: res = MCTS(chessboard, COLOR)
        if res[0] != -1: self.candidate_list.append(res)
        return res


@jit(nopython=True)
def get_candidate_list(chessboard, color):
    global n
    me = color
    op = -me
    idx = []
    for i in range(n):
        for j in range(n):
            if chessboard[i][j] == 0:
                idx.append((i, j))

    # get candidate_list
    res = []
    DIRS = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
    for x, y in idx:
        # find?
        fl = False
        for dx, dy in DIRS:
            if fl: break
            # ok?
            ok = True
            kx = x + dx
            ky = y + dy
            if is_out(kx, ky, n): continue

            if chessboard[kx][ky] == op:
                while chessboard[kx][ky] == op:
                    kx += dx
                    ky += dy
                    if is_out(kx, ky, n):
                        ok = False
                        break

                if is_out(kx, ky, n) or chessboard[kx][ky] != me:
                    ok = False

                if ok: fl = True

        if fl:
            res.append((x, y))
    return res


@jit(nopython=True)
def nxt(g, x, y, cur_player):
    op_player = -cur_player
    g[x][y] = cur_player
    DIRS = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
    for dx, dy in DIRS:
        if dx == 0 and dy == 0: continue

        ok = True
        kx = x + dx
        ky = y + dy
        if is_out(kx, ky, n): continue

        if g[kx][ky] == op_player:
            tx = kx
            ty = ky
            while g[kx][ky] == op_player:
                kx += dx
                ky += dy
                if is_out(kx, ky, n):
                    ok = False
                    break

            if is_out(kx, ky, n) or g[kx][ky] != cur_player:
                ok = False

            if ok:
                kx = tx
                ky = ty
                while g[kx][ky] == op_player:
                    g[kx][ky] = cur_player  # flip
                    kx += dx
                    ky += dy
    return g


@jit(nopython=True)
def result(g, color) -> int:
    n = len(g)
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == color:
                x += 1
            elif g[i][j] == -color:
                y += 1
    if x < y:
        return 1
    elif x == y:
        return 0
    elif x > y:
        return -1


@jit(nopython=True)
def simulate(g, u_col, fa_col) -> int:
    me_color = u_col
    op_color = -me_color
    cur_last = last

    vals = [
        [0, 20, 1, 2, 2, 1, 20, 0],
        [20, 2, 2, 4, 4, 2, 2, 20],
        [1, 2, 4, 8, 8, 4, 2, 1],
        [2, 4, 8, 0, 0, 8, 4, 2],
        [2, 4, 8, 0, 0, 8, 4, 2],
        [1, 2, 4, 8, 8, 4, 2, 1],
        [20, 2, 2, 4, 4, 2, 2, 20],
        [0, 20, 1, 2, 2, 1, 20, 0]
    ]

    while cur_last > 6:
        me_candi = get_candidate_list(g, me_color)
        if not me_candi:
            op_candi = get_candidate_list(g, op_color)
            if not op_candi:
                break
            else:
                me_candi = op_candi
                me_color = -me_color
                op_color = -op_color

        tmp = me_candi.copy()
        for tx, ty in tmp:
            for i in range(vals[tx][ty]):
                me_candi.append((tx, ty))

        tot = len(me_candi)
        x, y = me_candi[random.randint(0, tot-1)]

        cur_last -= 1

        g = nxt(g, x, y, me_color)
        me_color = -me_color
        op_color = -op_color

    res = dfs(me_color, g)
    if me_color == fa_col:
        return res
    else:
        return -res


def backup(u: Node, util):
    while u:
        u.n += 1
        u.w += util
        util = -util
        u = u.fa


def UCT(u: Node):
    C = 1.41
    if u.n == 0:
        return 0
    return u.w / u.n + C * np.sqrt(np.log(u.fa.n) / u.n)


def bestson(u: Node) -> Node:
    return max(u.sons, key=UCT)


def sel(root: Node) -> Node:
    leaf = bestson(root)
    while leaf.sons:
        leaf = bestson(leaf)
    return leaf


def expand(u: Node):
    candi = get_candidate_list(u.g, u.color)
    if not candi:
        u.sons.append(Node(copy.deepcopy(u.g), -u.color, u))
    else:
        for x, y in candi:
            son_g = nxt(copy.deepcopy(u.g), x, y, u.color)
            u.sons.append(Node(son_g, -u.color, u))


def op_sel_son(root: Node, cur_g, color) -> Node:
    if len(root.sons) == 1:
        return root.sons[0]
    else:
        for son in root.sons:
            if (son.g == cur_g).all():
                return son
        return Node(copy.deepcopy(cur_g), color, None)


def MCTS(chessboard, color):  # return the det pair
    global root, round_count
    round_count += 1

    start_time = time.time()

    if round_count == 1 or not root.sons:
        root = Node(copy.deepcopy(chessboard), color, None)
    else:
        root = op_sel_son(root, chessboard, color)

    candi = get_candidate_list(chessboard, color)
    if not candi:
        return -1, -1

    for x, y in candi:
        son_g = nxt(copy.deepcopy(chessboard), x, y, color)

        exist = False
        for cur_son in root.sons:
            if (cur_son.g == son_g).all():
                exist = True
                break
        if exist:
            continue

        son = Node(son_g, -color, root)
        root.sons.append(son)
        backup(son, simulate(son.g.copy(), son.color, son.fa.color))

    cnt = 0
    lim_time = 0
    if round_count == 1:
        lim_time = 3.7
    else:
        lim_time = 4.7
    while time.time() < start_time + lim_time:
        leaf = sel(root)
        expand(leaf)
        cnt += 1
        for son in leaf.sons:
            backup(son, simulate(son.g.copy(), son.color, son.fa.color))
    # print(cnt)

    val = -1
    res = (-1, -1)
    rec_son = Node(None, None, None)
    for i in range(len(candi)):
        x, y = candi[i]
        son = root.sons[i]

        nval = 2 * son.n + son.w
        if nval > val:
            val = nval
            rec_son = son
            res = (x, y)
    root = rec_son
    return res


@jit(nopython=True)
def dfs(color, g) -> int:
    candi = get_candidate_list(g, color)
    if not candi:
        op_candi = get_candidate_list(g, -color)
        if not op_candi:
            return result(g, color)
        return -dfs(-color, g)

    res = int(-1)
    for x, y in candi:
        son_g = nxt(g.copy(), x, y, color)
        t = -dfs(-color, son_g)
        if t == 1:
            return 1
        res = max(res, t)
    return res

if __name__ == '__main__':
    chessboard = np.array([[1, 1, 1, 1, 1, -1, -1, 0],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, -1, -1, 1, 1, 0, -1],
                           [1, 1, 1, -1, -1, -1, -1, -1],
                           [-1, 1, -1, -1, 1, -1, 1, 1],
                           [-1, -1, -1, 1, 1, 1, 1, 1],
                           [-1, -1, 1, 1, 1, 1, 1, 1],
                           [0, 0, 1, 0, 1, -1, -1, 1]])
    myAI = AI(8, 1, 5)
    print(myAI.go(chessboard))