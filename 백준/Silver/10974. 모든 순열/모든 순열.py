# 백트래킹

import sys


input = sys.stdin.readline
N = int(input())
stack = []
visited = [False] * (N+1)


def dfs():
    if len(stack) == N:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
        return
    for i in range(1, N+1):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            dfs()
            visited[i] = False
            stack.pop()


dfs()