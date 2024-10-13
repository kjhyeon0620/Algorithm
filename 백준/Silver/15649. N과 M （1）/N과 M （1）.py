def dfs():
    if len(stack) == M:
        print(*stack)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            dfs()
            stack.pop()
            visited[i] = False
            
            
N, M = map(int, input().split())
stack = []
visited = [False for _ in range(N+1)]
dfs()