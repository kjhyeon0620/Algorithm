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
            print(-1)
        elif op[4] == "f":
            print(deq.popleft())
        else:
            print(deq.pop())

    elif op[0] == "s":   # size
        print(size)
        
    elif op[0] == "e":   # empty
        if size == 0:
            print(1)
        else:
            print(0)
            
    elif op[0] == "f":   # front
        if size == 0:
            print(-1)
        else:
            print(deq[0])
            
    elif op[0] == "b":   # back
        if size == 0:
            print(-1)
        else:
            print(deq[size-1])
