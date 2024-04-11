# f(n) = f(n-1) + f(n-5) ( n >= 6)

def solution(num):
    if memo[num] != -1:
        return memo[num]
    memo[num] = solution(num-1) + solution(num-5)
    return memo[num]


T = int(input())
memo = [0, 1, 1, 1, 2, 2] + [-1] * 95

for _ in range(T):
    N = int(input())
    print(solution(N))
