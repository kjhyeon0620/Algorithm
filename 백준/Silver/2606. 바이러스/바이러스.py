# dfs

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)

visited = [1]
stack = [1]
while stack:
    el = stack.pop()
    for i in graph[el]:
        if i not in visited:
            visited.append(i)
            stack.append(i)
print(len(visited)-1)