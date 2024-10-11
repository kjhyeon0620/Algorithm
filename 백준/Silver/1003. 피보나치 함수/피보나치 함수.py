dp = [[-1, -1] for _ in range(41)]

dp[0], dp[1] = [1, 0], [0, 1]
ptr = 1

for _ in range(int(input())):
    N = int(input())
    
    if N > ptr:
        for i in range(ptr+1, N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
            
    print(*dp[N])
