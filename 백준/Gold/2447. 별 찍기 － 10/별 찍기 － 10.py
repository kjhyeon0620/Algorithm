# 시작 좌표와 n값을 입력받았을 때, n에 따라 가운데를 비워두고 나머지 부분은 n을 1 낮추고 다시 함수를 호출하여 구현한다.

import sys


def solution(x, y, num):
    if num == 1:
        return
    length = num // 3               # length => 한 변의 길이
    for i in range(3):
        for j in range(3):
            nx = x + (length * i)
            ny = y + (length * j)
            if i == 1 and j == 1:       # 가운데 부분은 전부 " "로 바꿔준다.
                for n in range(length):
                    for m in range(length):
                        board[nx + n][ny + m] = " "
            else:                       # 나머지 부분은 시작점과 num을 알맞게 바꿔 다시 함수를 호출한다.
                solution(nx, ny, length)


N = int(input())
board = [["*" for _ in range(N)] for _ in range(N)]

solution(0, 0, N)
for a in range(N):
    sys.stdout.write("".join(board[a]) + "\n")
