# dp를 이용해 해결한다.

dp = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]


def solution(n1, n2, n3):
    if n1 <= 0 or n2 <= 0 or n3 <= 0:
        return 1
    if n1 > 20 or n2 > 20 or n3 > 20:
        return solution(20, 20, 20)
    if dp[n1][n2][n3] != -1:
        return dp[n1][n2][n3]
    if n1 < n2 < n3:
        dp[n1][n2][n3] = solution(n1, n2, n3-1) + solution(n1, n2-1, n3-1) - solution(n1, n2-1, n3)
        return dp[n1][n2][n3]

    dp[n1][n2][n3] = solution(n1-1, n2, n3) + solution(n1-1, n2-1, n3) + solution(n1-1, n2, n3-1) - solution(n1-1, n2-1, n3-1)
    return dp[n1][n2][n3]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {solution(a, b, c)}')


