n = int(input())

dp = [-1 for _ in range(n+1)]
dp[0], dp[1] = 1, 1


def topDown(num):
    if dp[num] != -1:
        return dp[num]
    dp[num] = (topDown(num-1) + 2 * topDown(num-2)) % 10007
    return dp[num]


print(topDown(n))