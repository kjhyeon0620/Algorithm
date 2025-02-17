# bfs를 통해 각 위치의 토마토가 익을 때까지 걸리는 날짜를 기록한다.
# 기록된 값중 최댓값이 모든 토마토가 익을 때까지 걸리는 최소 날짜이다.
# 다만, 값 중에 0이 있을 경우 익을 수 없는 토마토가 있는 경우이므로 -1을 출력한다.

import sys
from collections import deque


input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
q = deque()

for i in range(N):      # 익은 토마토 큐에 집어넣기
    for j in range(M):
        if board[i][j] == 1:
            q.append([i, j])

while q:                # bfs를 통해 날짜 계산하기
    node = q.popleft()
    y, x = node[0], node[1]
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
            board[ny][nx] = board[y][x] + 1
            q.append([ny, nx])

ans = -1

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, board[i][j])

print(ans-1)
