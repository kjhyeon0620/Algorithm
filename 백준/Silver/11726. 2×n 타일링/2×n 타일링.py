# f(n) = f(n-1)(1x2 타일 + 나머지) + f(n-2)(2x1 타일 + 나머지)

n = int(input())
dp = [0, 1, 2] * n  # n-1 크기로 해도 d[n]을 사용할 수 있지만 n이 1일 경우를 위해 * n 으로 설정
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])