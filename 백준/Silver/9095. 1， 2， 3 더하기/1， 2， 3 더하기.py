import sys


input = sys.stdin.readline

dp = [-1 for _ in range(11)]
dp[1], dp[2], dp[3] = 1, 2, 4

def topDown(num):
    if dp[num] != -1:
        return dp[num]
    dp[num] = topDown(num-1) + topDown(num-2) + topDown(num-3)
    return dp[num]


for _ in range(int(input())):
    print(topDown(int(input())))
