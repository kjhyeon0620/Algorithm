# f(n)은 n 번째 계단까지의 계단을 오르는 경우의 수 중 규칙을 만족하는 경우의 최댓값이다.
# f(n) = max(f(n-3) + score[n-1] + score[n], f(n-2) + score[n]) 이다.
# f(0) = 0
# f(1) = score[1]
# f(2) = f(1) + score[2]
# f(3) = max(f(0) + score[2] + score[3], f(1) + score[3])

import sys


def solution(num):
    if memo[num] != -1:
        return memo[num]
    memo[num] = score[num] + max(solution(num-3) + score[num-1], solution(num-2))
    return memo[num]


input = sys.stdin.readline
n = int(input())
score = [0] + [int(input()) for _ in range(n)]
if n == 1:
    print(score[1])
else:
    memo = [-1] * (n+1)
    memo[0], memo[1], memo[2] = 0,  score[1], score[1]+score[2]

    print(solution(n))
