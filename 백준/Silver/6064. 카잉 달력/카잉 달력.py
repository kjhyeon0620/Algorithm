# 최대 공약수를 구하여 마지막 해를 알아낸 후, 마지막 해의 이전까지 유효한 해를 구한다.

import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    if M < N:
        M, N = N, M
        x, y = y, x

    tmp = 0
    maxTmp = M * N // gcd(M, N) // M

    while True:
        if tmp > maxTmp:
            print(-1)
            break
        if (M * tmp + x - 1) % N + 1 == y:
            print(M * tmp + x)
            break
        tmp += 1

