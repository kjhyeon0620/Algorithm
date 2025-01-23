import sys


input = sys.stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[cost[0][0], cost[0][1], cost[0][2]] for _ in range(N)]

for home in range(1, N):
    for color in range(3):
        dp[home][color] = cost[home][color] + min(dp[home-1][(color+1) % 3], dp[home-1][(color+2) % 3])

print(min(dp[N-1]))
