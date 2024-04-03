# 집합을 이용해 주어진 연산을 수행한다.

import sys


input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    op = input().strip()
    if op == "all":
        S = set(range(1, 21))

    elif op == "empty":
        S = set()

    else:
        op, num = op.split()
        num = int(num)

        if op == "add":
            S.add(num)

        elif op == "remove" and num in S:
            S.discard(num)

        elif op == "check":
            if num in S:
                sys.stdout.write("1\n")
            else:
                sys.stdout.write("0\n")

        elif op == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)


