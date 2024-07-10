# dfs를 통해 한 번에 해킹할 수 있는 컴퓨터의 수를 탐색한다.

import sys


input = sys.stdin.readline

N, M, = map(int, input().split())
graph = [[] for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n2].append(n1)


def dfs(num):
    stack = []
    visited = [False] * (N+1)
    for e in graph[num]:
        stack.append(e)
    if stack:
        cnt[num] = 1
    while stack:
        node = stack.pop()
        for el in graph[node]:
            if not visited[el]:
                stack.append(el)
                visited[el] = True
                cnt[num] += 1


stack = []
for i in range(1, N+1):
    visited = [False] * (N+1)
    stack.append(i)
    visited[i] = True

    while stack:
        node = stack.pop()
        for el in graph[node]:
            if not visited[el]:
                stack.append(el)
                visited[el] = True
                cnt[i] += 1

maxValue = max(cnt)

for i in range(1, N+1):
    if cnt[i] == maxValue:
        print(i, end=" ")
