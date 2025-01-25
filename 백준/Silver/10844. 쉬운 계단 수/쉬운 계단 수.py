N = int(input())
dp = [[0 for _ in range(11)] for _ in range(N+1)]

for a in range(1, 10):
    dp[1][a] = 1
for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
