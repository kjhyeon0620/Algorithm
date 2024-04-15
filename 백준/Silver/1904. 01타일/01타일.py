# f(n) = f(n-1) + f(n-2) 이다. (f(n-1) = 1타일을 쓰고 나머지 , f(n-2) = 00타일을 쓰고 나머지)

N = int(input())
dp = [-1] * (N+2)   # N == 1 일 때를 위해 (N+2) 크기로 생성
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])