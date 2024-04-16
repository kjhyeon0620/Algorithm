# dfs를 이용해 모든 땅을 검사한다.

import sys


def dfs(x, y):
    if visited[y][x]:
        return
    visited[y][x] = True
    if x > 0 and board[y][x-1] == 1:
        dfs(x-1, y)
    if x < M-1 and board[y][x+1] == 1 :
        dfs(x+1, y)
    if y > 0 and board[y-1][x] == 1:
        dfs(x, y-1)
    if y < N-1 and board[y+1][x] == 1:
        dfs(x, y+1)


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1
        
    cnt = 0
    
    for i in range(M):
        for j in range(N):
            if board[j][i] and not visited[j][i]:
                dfs(i, j)
                cnt += 1
    print(cnt)