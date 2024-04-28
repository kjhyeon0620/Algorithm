# "해당 위치에서 도착점까지 최소 거리"가 저장된 리스트를 dp를 이용해 생성한다.

from collections import deque

N, M = map(int, input().split())
maze = [[] for _ in range(N)]

for i in range(N):
    for el in input():
        maze[i].append(el)
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dp[N-1][M-1] = 1
queue = deque()
queue.append([N-1, M-1])

while queue:
    node = queue.popleft()
    y, x = node[0], node[1]
    for i in range(4):
        if (0 <= x + dx[i] < M and 0 <= y + dy[i] < N
                and dp[y + dy[i]][x + dx[i]] == -1 and maze[y + dy[i]][x + dx[i]] == "1"):
            queue.append([y + dy[i], x + dx[i]])
            dp[y + dy[i]][x + dx[i]] = dp[y][x] + 1

print(dp[0][0])
