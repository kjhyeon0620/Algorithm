# dp를 이용해 팩토리얼을 구하고, 이를 이용해 이항 계수를 구한다.

N, K = map(int, input().split())
memo = [-1 for _ in range(N+1)]


def factorial(num):
    if memo[num] != -1:
        return memo[num]
    memo[num] = factorial(num-1) * num
    return memo[num]


memo[0], memo[1] = 1, 1
print(factorial(N) // (factorial(N-K) * factorial(K)) % 10007)

