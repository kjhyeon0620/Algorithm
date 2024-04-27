# dfs를 이용하여 해결한다.

import sys


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
stack = []


def dfs(start):
    if len(stack) == M:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
        return

    prev = 0
    for i in range(start, N):
        if prev != A[i]:
            stack.append(A[i])
            prev = A[i]
            dfs(i)
            stack.pop()


dfs(0)