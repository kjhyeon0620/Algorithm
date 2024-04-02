# 101 x 101의 배열에 색종이가 포함된 영역을 표시한다.

N = int(input())
board = [[0] * 101 for _ in range(101)]
cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if board[x+i][y+j] == 0:
                cnt += 1
                board[x+i][y+j] = 1

print(cnt)