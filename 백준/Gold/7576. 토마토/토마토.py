from collections import deque

M, N = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = -1
q = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            q.append([i, j])

if len(q) == 0:
    print(-1)
else:
    while q:
        ans += 1
        for el in range(len(q)):
            node = q.popleft()
            y, x = node[0], node[1]
            for a in range(4):
                ny = y + dy[a]
                nx = x + dx[a]
                if 0 <= ny < N and 0 <= nx < M and tomatoes[ny][nx] == 0:
                    tomatoes[ny][nx] = 1
                    q.append([ny, nx])

    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:
                print(-1)
                exit(0)
    print(ans)
