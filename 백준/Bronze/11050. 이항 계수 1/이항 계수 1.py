# 팩토리얼을 구하는 함수를 만들고 이를 이용해 이항 계수를 구한다.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    if memo[num] != 0:
        return memo[num]
    memo[num] = num * factorial(num-1)
    return memo[num]


memo = [0] * 11
N, K = map(int, input().split())

print(factorial(N) // (factorial(K) * factorial(N-K)))
