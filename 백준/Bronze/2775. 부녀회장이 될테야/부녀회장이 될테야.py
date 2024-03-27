# 0층 -> 1 2 3 4 5 6 ..
# 1층 -> 1 3 6 10 15 21
# 2층 -> 1 4 10 20 35 56
# k층의 n호 -> k층의 (n-1호) + (k-1)층의 n호

def solution(a, b):  # a는 층, b는 호
    if memo[a][b] != 0:
        return memo[a][b]
    if a == 0:
        return b
    if b == 1:
        return 1
    memo[a][b] = solution(a, b-1) + solution(a-1, b)
    return memo[a][b]


T = int(input())
memo = [[0] * 15 for _ in range(15)]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(solution(k, n))
