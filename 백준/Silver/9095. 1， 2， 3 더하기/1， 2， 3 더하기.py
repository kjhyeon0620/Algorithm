# 합의 개수를 구하는 함수를 f라고 하면
# f(1) = 1, f(2) = f(1) + 1(2로만 구성), f(3) = f(1) + f(2) + 1(3으로만 구성)
# f(4) = f(1) + f(2) + f(3), f(n) = f(n-1) + f(n-2) + f(n-3)

def solution(num):
    if memo[num] != -1:
        return memo[num]
    memo[num] = solution(num-1) + solution(num-2) + solution(num-3)
    return memo[num]

T = int(input())
memo = [0, 1, 2, 4] + [-1] * 28

for _ in range(T):
    print(solution(int(input())))