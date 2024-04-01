# M개의 사이트 중에서 N개를 고르면 사이트가 자동으로 연결된다.
# 따라서 mCn을 계산하면 된다.

def factorial(num):
    if memo[num] != 0:
        return memo[num]
    if num == 0:
        return 1
    memo[num] = num * factorial(num-1)
    return memo[num]


memo = [0] * 31

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(N) * factorial(M-N)))