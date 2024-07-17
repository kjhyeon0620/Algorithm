# dp를 이용하여 답을 구한다.
# i 행까지의 물건을 이용하여 j 무게 만큼까지 담을 수 있을 때 최댓값이 dp[i][j]이다.
# j가 해당 물건의 무게보다 낮을 때 dp[i][j]는 이전 행의 dp, 즉 dp[i-1][j]이다.
# 이외의 경우에는 해당 물건과 k에서 해당 물건의 무게를 뺀 값의 dp / 이전 행의 dp값 중 최댓값이 dp값이다.
# 즉, dp[i][j] = max(stuff[i][1] + dp[i-1][j-stuff[i][0]], dp[i-1][j]) 이다.

import sys


input = sys.stdin.readline
N, K = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= stuff[i-1][0]:
            dp[i][j] = max(stuff[i-1][1] + dp[i-1][j-stuff[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])