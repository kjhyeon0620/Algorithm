# list를 이용하여 주어진 명령을 수행한다.

import sys


input = sys.stdin.readline
N = int(input())
stack = []
cnt = 0

for _ in range(N):
    op = input()
    if op[0] == "p" and op[1] == "u":
        op, num = op.split()
        num = int(num)
        stack.append(num)
        cnt += 1

    elif op[0] == "p":
        if cnt == 0:
            print(-1)
        else:
            print(stack.pop())
            cnt -= 1

    elif op[0] == "s":
        print(cnt)

    elif op[0] == "e":
        print(1 if cnt == 0 else 0)

    else:
        if cnt == 0:
            print(-1)
        else:
            print(stack[-1])

