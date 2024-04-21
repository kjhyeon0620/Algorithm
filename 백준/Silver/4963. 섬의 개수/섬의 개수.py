# 섬의 정보를 그래프에 저장한 후 bfs를 이용해 모든 섬을 방문하여 개수를 센다.

import sys
from collections import deque


def isMovable(x, y, _w, _h):
    return 0 <= x < _w and 0 <= y < _h


input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    diff = [-1, 0, 1]

    if w == 0 or h == 0:
        break

    board = []

    for k in range(h):
        board.append(list(map(int, input().split())))

    cnt = 0
    queue = deque()

    for i in range(w):
        for j in range(h):
            if board[j][i] == 1:
                board[j][i] = 0
                queue.append([i, j])
                cnt += 1
                while queue:
                    node = queue.popleft()
                    nodeI, nodeJ = node[0], node[1]
                    for iDiff in diff:
                        for jDiff in diff:
                            if (isMovable(nodeI + iDiff, nodeJ + jDiff, w, h)
                                    and board[nodeJ + jDiff][nodeI + iDiff]):
                                queue.append([nodeI+iDiff, nodeJ+jDiff])
                                board[nodeJ+jDiff][nodeI+iDiff] = 0
    print(cnt)

