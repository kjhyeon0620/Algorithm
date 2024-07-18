# 우선 색깔별로 탐색하여 구역의 수를 센다.
# 적록색약의 경우 R을 전부 G로 바꾼 후 구역을 다시 센다.

import sys


input = sys.stdin.readline
N = int(input())
board = [list(input()) for _ in range(N)]


def solution(area):
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                stack = [[i, j]]
                while stack:
                    node = stack.pop()
                    x, y = node[0], node[1],
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and area[i][j] == area[nx][ny] and not visited[nx][ny]:
                            stack.append([nx, ny])
                            visited[nx][ny] = True
    print(cnt, end=" ")


solution(board)
for i in range(N):
    for j in range(N):
        if board[i][j] == "R":
            board[i][j] = "G"
solution(board)