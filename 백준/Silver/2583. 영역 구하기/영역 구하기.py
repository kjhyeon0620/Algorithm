# 직사각형 내부의 점을 계산한 뒤, 영역 외부의 점을 bfs로 탐색하여 넓이를 구한다.

from collections import deque


M, N, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
squares = []

for _ in range(K):
    squares.append(list(map(int, input().split())))

for square in squares:
    for x in range(square[0], square[2]):
        for y in range(square[1], square[3]):
            board[x][y] = 1

areas = []
visited = [[False] * N for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            cnt = 0
            queue = deque()
            queue.append([i, j])

            while queue:
                tx, ty = queue.popleft()

                cnt += 1
                board[tx][ty] = 1
                for k in range(4):
                    X = tx + dx[k]
                    Y = ty + dy[k]
                    if 0 <= X < N and 0 <= Y < M and board[X][Y] == 0:
                        board[X][Y] = 1
                        queue.append([X, Y])

            areas.append(cnt)

print(len(areas))
print(*sorted(areas))


