# bfs를 이용하여 그래프를 탐색하고, 깊이를 이용하여 각 노드의 부모를 저장한다.

import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
parent = [-1 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
depth = 0
queue = deque()
queue.append(1)

while queue:
    node = queue.popleft()
    visited[node] = True
    for el in graph[node]:
        if not visited[el]:
            queue.append(el)
            parent[el] = node

for i in range(2, N+1):
    sys.stdout.write(str(parent[i]) + "\n")

