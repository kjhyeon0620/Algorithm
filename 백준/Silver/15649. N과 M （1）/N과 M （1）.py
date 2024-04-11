# dfs로 구한다.

import sys


def dfs():
    if len(stack) == M:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
    for i in range(1, N+1):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            dfs()
            visited[i] = False
            stack.pop()


N, M = map(int, input().split())
arr = list(range(1, N+1))
visited = [False for _ in range(N+1)]
stack = []
dfs()
