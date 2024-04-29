# dfs를 이용하여 이동할 단지 수를 계산한다.

N = int(input())
board = []
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    board.append(input())
cnt = 0
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == "1":
            cnt += 1
            tmp = 1
            visited[i][j] = True
            stack = [[i, j]]
            while stack:
                node = stack.pop()
                n1, n2 = node[0], node[1]

                for d in range(4):
                    nx = n1 + dx[d]
                    ny = n2 + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == "1":
                        tmp += 1
                        visited[nx][ny] = True
                        stack.append([nx, ny])
            ans.append(tmp)
ans.sort()
print(cnt)
for num in ans:
    print(num)

