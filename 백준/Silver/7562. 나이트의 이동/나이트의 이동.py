# bfs 를 이용하여 도착지까지 한 칸씩 이동한다.

import sys
from collections import deque


input = sys.stdin.readline
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

for _ in range(int(input())):
    I = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    memo = [[-1 for _ in range(I)] for _ in range(I)]
    memo[x1][y1] = 0
    queue = deque()
    queue.append([x1, y1])

    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            print(memo[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and memo[nx][ny] == -1:
                memo[nx][ny] = memo[x][y] + 1
                queue.append((nx, ny))
