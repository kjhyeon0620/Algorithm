def solution(num):
    if num < 0:
        return 0
    if dp[num] != -1:
        return dp[num]
    dp[num] = max(score[num-1] + solution(num-3), solution(num-2)) + score[num]
    return dp[num]


N = int(input())
score = [int(input()) for _ in range(N)]

dp = [-1 for _ in range(N)]
dp[0] = score[0]

print(solution(N-1))