# 각 칸에서 목적지까지 도달할 수 있는 경우의 수를 dp를 이용하여 기록한다.

import sys


input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[N-1][N-1] = 1

for a in range(N-2, -1, -1):
    if a + board[N-1][a] < N:
        dp[N-1][a] = dp[N-1][a+board[N-1][a]]
    if a + board[a][N-1] < N:
        dp[a][N-1] = dp[a+board[a][N-1]][N-1]
for i in range(N-2, -1, -1):
    for j in range(N-2, -1, -1):
        if i + board[i][j] < N:
            dp[i][j] += dp[i+board[i][j]][j]
        if j + board[i][j] < N:
            dp[i][j] += dp[i][j+board[i][j]]

print(dp[0][0])