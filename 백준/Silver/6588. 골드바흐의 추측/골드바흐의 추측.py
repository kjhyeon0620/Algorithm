# 3부터 시작하여 두 홀수 소수의 합으로 나타낼 수 있는지 확인한다.
# dp를 이용하여 소수 확인을 중복으로 처리하지 않도록 한다.

import sys


def isPrimeNum(num):
    if dp[num] != -1:
        return dp[num]
    for a in range(2, int(num ** 0.5) + 1):
        if num % a == 0:
            dp[num] = False
            return dp[num]
    dp[num] = True
    return dp[num]


input = sys.stdin.readline
dp = [-1] * (10**6 + 1)
while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    for i in range(3, n // 2 + 1, 2):
        if isPrimeNum(i) and isPrimeNum(n - i):
            ans = i
            break
    if ans == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f"{n} = {ans} + {n - ans}")