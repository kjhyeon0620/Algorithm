# dp의 bottom-up을 이용하여 각 집의 색깔별로 최솟값을 저장해둔다.

import sys


input = sys.stdin.readline
N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))
dp = [[-1, -1, -1] for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]

for i in range(1, N):
    for j in range(3):
        tmp = []
        for k in range(3):                # 해당 집을 특정 색깔로 칠했을 때,
            if j != k:                    # 이전 집의 dp의 값중 같은 색깔을 제외한 후
                tmp.append(dp[i-1][k])    # 작은 값을 골라 dp에 저장한다.
        dp[i][j] = costs[i][j] + min(tmp)

print(min(dp[N-1]))
