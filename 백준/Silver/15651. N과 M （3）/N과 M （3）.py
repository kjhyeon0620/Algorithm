# 백트래킹을 이용해 해결한다.

import sys


N, M = map(int, input().split())
stack = []


def dfs():
    if len(stack) == M:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
        return
    for i in range(1, N+1):
        stack.append(i)
        dfs()
        stack.pop()


dfs()