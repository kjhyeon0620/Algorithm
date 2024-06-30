# BFS를 이용해 케빈 베이컨의 수를 구한다.

import sys
from collections import deque

input = sys.stdin.readline
N, M, = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = [N*N] + [0] * N   # 1부터 시작하므로 N+1 크기의 리스트를 만든다.
                        # 최솟값을 구할 때 0번째 인덱스가 답이 되지 않도록 큰 값을 넣어준다.

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, N+1):
    visited = [False] * (N+1)
    tmp = 1
    queue = deque()
    queue.append(i)

    while queue:                # depth에 맞춰 tmp에 값을 더한다.
        length = len(queue)
        for _ in range(length):
            node = queue.popleft()
            visited[node] = True
            for num in graph[node]:
                if not visited[num]:
                    ans[i] += tmp
                    visited[num] = True
                    queue.append(num)

        tmp += 1

print(ans.index(min(ans)))