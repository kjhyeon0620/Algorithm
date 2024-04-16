# stack으로 dfs, queue로 bfs를 구현한다

import sys
from collections import deque


input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2, = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# dfs

visitedDfs = [False] * (N+1)
stack = [V]
ansDfs = []

while stack:
    node = stack.pop()
    if visitedDfs[node]:
        continue
    graph[node].sort(reverse=True)
    ansDfs.append(node)
    visitedDfs[node] = True

    for el in graph[node]:
        if not visitedDfs[el]:
            stack.append(el)

# bfs

visitedBfs = [False] * (N+1)
queue = deque()
ansBfs = []
queue.append(V)

while queue:
    node = queue.popleft()
    if visitedBfs[node]:
        continue
    visitedBfs[node] = True
    ansBfs.append(node)
    graph[node].sort()

    for el in graph[node]:
        if not visitedBfs[el]:
            queue.append(el)
            
sys.stdout.write(" ".join(map(str, ansDfs)) + "\n")
sys.stdout.write(" ".join(map(str, ansBfs)))
