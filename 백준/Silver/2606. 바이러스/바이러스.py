N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

stack = [1]
visited = [False for _ in range(N+1)]
visited[1] = True
ans = -1
while stack:
    node = stack.pop()
    ans += 1
    for el in graph[node]:
        if not visited[el]:
            visited[el] = True
            stack.append(el)

print(ans)
