import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

flag = False
goal = []
for i in range(n):
    if flag:
        break
    for j in range(m):
        if board[i][j] == 2:
            goal = [i, j]
            flag = True
            break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append(goal)
cnt = [[0] * m for _ in range(n)]
while q:
    for _ in range(len(q)):
        el = q.popleft()
        x = el[1]
        y = el[0]
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                board[ny][nx] = 0
                cnt[ny][nx] = cnt[y][x] + 1
                q.append([ny, nx])

for k in range(n):
    for l in range(m):
        if cnt[k][l] == 0 and board[k][l] == 1:
            print(-1, end=" ")
        else:
            print(cnt[k][l], end=" ")
    print()
