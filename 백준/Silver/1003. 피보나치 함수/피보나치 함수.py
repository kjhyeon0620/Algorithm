# 0 -> 1 0 / 1 -> 0 1 / 2 -> n(0) + n(1) / 3 -> n(2) + n(1)
# 0: 1 0 1 1 2 3 5 8...
# 1: 0 1 1 2 3 5 8 13 ...
# 1, 1, 2, 3 ... 로 이뤄진 피보나치 수열을 이용해 0과 1의 횟수를 구한다.

def fibonacci(num):
    if memo[num] != -1:
        return memo[num]
    memo[num] = fibonacci(num-1) + fibonacci(num-2)
    return memo[num]

T = int(input())
memo = [0, 1, 1] + [-1] * 38

for _ in range(T):
    N = int(input())
    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        print(fibonacci(N-1), fibonacci(N))