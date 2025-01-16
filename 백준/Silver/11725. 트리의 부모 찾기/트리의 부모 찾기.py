from collections import deque
import sys


input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

visited = [False for _ in range(N+1)]
ans = [-1 for _ in range(N+1)]
queue = deque([1])

while queue:
    node = queue.popleft()
    visited[node] = True
    for el in tree[node]:
        if not visited[el]:
            ans[el] = node
            queue.append(el)

for i in range(2, N+1):
    print(ans[i])