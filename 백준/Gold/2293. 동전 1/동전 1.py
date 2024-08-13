# 2차원 dp를 이용하여 해결한다.
# dp[i][j]는 i번째 코인까지 사용하여 j의 가치를 만들 수 있는 경우의 수이다.

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [[0 for _ in range(k+1)] for _ in range(2)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if coins[i-1] == j:
            dp[i % 2][j] = dp[(i+1) % 2][j] + 1
        elif coins[i-1] <= j:
            dp[(i % 2)][j] = dp[(i+1) % 2][j] + dp[i % 2][j-coins[i-1]]
        else:
            dp[i % 2][j] = dp[(i+1) % 2][j]

print(dp[n % 2][k])