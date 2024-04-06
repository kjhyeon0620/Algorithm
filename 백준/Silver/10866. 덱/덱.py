# deque를 이용하여 덱을 구현한다

import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
deq = deque()
size = 0

for _ in range(N):
    op = input()
    if op[1] == "u":     # push ~
        op, num = op.split()
        size += 1
        if op[5] == "f": # push_front
            deq.appendleft(num)
        else:            # push_back
            deq.append(num)

    elif op[0] == "p":   # pop ~
        size -= 1
        if size == -1:
            size = 0
            sys.stdout.write("-1\n")
        elif op[4] == "f":
            sys.stdout.write(str(deq.popleft()) + "\n")
        else:
            sys.stdout.write(str(deq.pop()) + "\n")

    elif op[0] == "s":   # size
        sys.stdout.write(str(size) + "\n")

    elif op[0] == "e":   # empty
        if size == 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")

    elif op[0] == "f":   # front
        if size == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(deq[0]) + "\n")

    elif op[0] == "b":   # back
        if size == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(deq[size-1]) + "\n")
