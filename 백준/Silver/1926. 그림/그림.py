# dfs를 이용하여 그림의 개수와 넓이를 구한다.

import sys


input = sys.stdin.readline
n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

cnt = 0
areas = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = 0
            cnt += 1
            stack = [[i, j]]
            tmp = 0
            while stack:
                node = stack.pop()
                y, x = node[0], node[1]
                tmp += 1
                for a in range(4):
                    ny = y + dy[a]
                    nx = x + dx[a]
                    if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                        board[ny][nx] = 0
                        stack.append([ny, nx])
            areas.append(tmp)

print(cnt)
if len(areas) == 0:
    print(0)
else:
    print(max(areas))