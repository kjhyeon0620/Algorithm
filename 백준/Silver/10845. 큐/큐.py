# deque를 이용하여 큐를 구현한다.
from collections import deque
import sys

input = sys.stdin.readline
queue = deque()
cnt = 0
N = int(input())

for _ in range(N):
    op = input()
    
    if op[1] == "u":
        op, num = op.split()
        queue.append(num)
        cnt += 1

    elif op[0] == "p":
        if cnt == 0:
            print(-1)
        else:
            print(queue.popleft())
            cnt -= 1

    elif op[0] == "s":
        print(cnt)

    elif op[0] == "e":
        if cnt == 0:
            print(1)
        else:
            print(0)

    elif op[0] == "f":
        if cnt == 0:
            print(-1)
        else:
            print(queue[0])

    elif op[0] == "b":
        if cnt == 0:
            print(-1)
        else:
            print(queue[cnt-1])