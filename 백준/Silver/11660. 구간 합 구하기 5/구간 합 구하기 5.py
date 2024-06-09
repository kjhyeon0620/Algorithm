# dp를 이용하여 (1,1)부터 (x,y)까지의 합을 전부 계산해둔 후, 이를 이용해 답을 구한다.

import sys


input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(N)]
dp[0][0] = board[0][0]

for i in range(1, N):
    dp[0][i] = dp[0][i-1] + board[0][i]

for j in range(1, N):
    dp[j][0] = dp[j-1][0] + board[j][0]

for i in range(1, N):
    for j in range(1, N):
        dp[j][i] = dp[j-1][i] + dp[j][i-1] + board[j][i]-dp[j-1][i-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x2 == 1 or y2 == 1:
        print(dp[x2-1][y2-1] - dp[x1-1][y1-1]+board[x1-1][y1-1])
    elif x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2])
    elif y1 == 1:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1])
    else:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1] - dp[x2-1][y1-2] + dp[x1-2][y1-2])

