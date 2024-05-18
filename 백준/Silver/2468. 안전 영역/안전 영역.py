# dfs를 통해 해결한다.

import sys


input = sys.stdin.readline

N = int(input())
region = []
for _ in range(N):
    region.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = [1]

for h in range(1, 100):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if region[i][j] > h and not visited[i][j]:
                cnt += 1
                stack = [[i, j]]
                while stack:
                    node = stack.pop()
                    x, y, = node[1], node[0]
                    if not (0 <= x < N and 0 <= y < N) or visited[y][x] or region[y][x] <= h:
                        continue
                    visited[y][x] = True
                    for k in range(4):
                        stack.append([y+dy[k], x+dx[k]])
    if cnt == 0:
        break
    ans.append(cnt)

print(max(ans))
