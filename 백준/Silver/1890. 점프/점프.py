import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

direction = [(1, 0), (0, 1)]    # 하 우
dp = [[-1]*N for _ in range(N)]

def dfs(x, y):
    if x == N-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for d in direction:
            nx = x + d[0] * graph[x][y]
            ny = y + d[1] * graph[x][y]
            if 0 <= nx < N and 0 <= ny < N:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))