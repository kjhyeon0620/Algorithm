# deque를 이용해 큐를 구현한다.

import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
size = 0

N = int(input())

for _ in range(N):
    op = input().strip()
    if op[1] == "u":    # push X
        op, num = op.split()
        queue.append(num)
        size += 1

    elif op[0] == "p":  # pop
        if size == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(queue.popleft() + "\n")
            size -= 1

    elif op[0] == "s":  # size
        sys.stdout.write(str(size) + "\n")

    elif op[0] == "e":  # empty
        if size == 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif op[0] == "f":  # front
        if size == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(queue[0] + "\n")

    else:               # back
        if size == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(queue[size-1] + "\n")