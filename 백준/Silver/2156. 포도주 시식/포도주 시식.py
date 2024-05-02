# dp를 이용하여 해결한다.

import sys

input = sys.stdin.readline
n = int(input())
wines = []

for _ in range(n):
    wines.append(int(input()))

if n == 1:
    print(wines[0])

elif n == 2:
    print(wines[0] + wines[1])

else:
    dp = [-1 for _ in range(n)]
    dp[0] = wines[0]
    dp[1] = wines[1] + wines[0]
    dp[2] = max(wines[2] + wines[0], wines[2] + wines[1], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-1], wines[i] + wines[i-1] + dp[i-3], wines[i] + dp[i-2])

    print(dp[-1])