# 익은 토마토로부터 bfs를 실행하여 각 토마토가 익는 날짜를 계산한다.
from collections import deque
import sys


input = sys.stdin.readline
M, N, H = map(int, input().split())
board = [[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        board[i].append(list(map(int, input().split())))

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append([i, j, k])

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
while q:
    node = q.popleft()
    x, y, z = node[2], node[1], node[0]
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and board[nz][ny][nx] == 0:
            board[nz][ny][nx] = board[z][y][x] + 1
            q.append([nz, ny, nx])
ans = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                ans = max(ans, board[i][j][k])

print(ans-1)
