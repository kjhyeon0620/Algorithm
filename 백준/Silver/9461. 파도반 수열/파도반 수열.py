dp = [0, 1, 1, 1, 2, 2] + [-1 for _ in range(95)]
cnt = 5

for _ in range(int(input())):
    N = int(input())
    if dp[N] != -1:
        cnt = max(cnt, N)
    else:
        for i in range(cnt+1, N+1):
            dp[i] = dp[i-1] + dp[i-5]
        cnt = N
        
    print(dp[N])
