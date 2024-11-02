N, K = map(int, input().split())
dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]


def solution(n, k):
    if dp[n][k] != -1:
        return dp[n][k]
    if k == 1 or n == 0:
        return 1

    dp[n][k] = (solution(n - 1, k) + solution(n, k - 1)) % 1000000000
    return dp[n][k]


print(solution(N, K))
