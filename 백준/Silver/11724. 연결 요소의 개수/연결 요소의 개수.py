# dfs를 이용하여 연결 요소의 개수를 센다

import sys


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
stack = []
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if visited[i]:
        continue
    stack.append(i)
    cnt += 1

    while stack:
        node = stack.pop()
        visited[node] = True

        for el in graph[node]:
            if not visited[el]:
                stack.append(el)

print(cnt)