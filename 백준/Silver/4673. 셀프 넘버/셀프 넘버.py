# d(n) 함수를 정의한다.
# 10036 크기의 리스트를 만든 후 전부 True로 초기화한다. (d(9999) = 10035)
# 1부터 10000까지 d(n)을 실행시켜 나온 수를 위 리스트에서 False로 바꾼다.

import sys


def dNum(num):
    res = num

    while num > 0:
        res += num % 10
        num //= 10

    return res


isSelfNums = [True] * 10036

for i in range(1, 10001):
    isSelfNums[dNum(i)] = False

for i in range(1, 10001):
    if isSelfNums[i]:
        sys.stdout.write(str(i) + "\n")
