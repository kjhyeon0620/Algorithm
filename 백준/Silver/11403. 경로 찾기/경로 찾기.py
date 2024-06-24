# bfs 를 통해 각 행의 경로를 각각 찾는다.

import sys
from collections import deque


input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(x):
    queue = deque()
    queue.append(x)
    visited = [0] * N
    while queue:
        node = queue.popleft()

        for i in range(N):
            if not visited[i] and graph[node][i]:
                queue.append(i)
                visited[i] = 1
    return visited


for i in range(N):
    print(*bfs(i))
