N = int(input())

height = [list(map(int, input().split())) for _ in range(N)]
ans = [1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for h in range(1, 99):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and height[x][y] > h:
                cnt += 1
                stack = [[x, y]]
                visited[x][y] = True
                while stack:
                    node = stack.pop()
                    sx, sy = node[0], node[1]
                    for i in range(4):
                        nx = sx + dx[i]
                        ny = sy + dy[i]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and height[nx][ny] > h:
                            stack.append([nx, ny])
                            visited[nx][ny] = True
    if cnt == 0:
        break
    ans.append(cnt)

print(max(ans))

