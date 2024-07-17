# 시작 좌표와 n값을 입력받았을 때, n에 따라 가운데를 비워두고 나머지 부분은 n을 1 낮추고 다시 함수를 호출하여 구현한다.

import sys


def solution(x, y, num):
    if num == 0:
        return
    length = 3 ** (num-1)               # length => 한 변의 길이
    for i in range(3):
        for j in range(3):
            nx = x + (length * i)
            ny = y + (length * j)
            if i == 1 and j == 1:       # 가운데 부분은 전부 " "로 바꿔준다.
                for n in range(length):
                    for m in range(length):
                        board[nx + n][ny + m] = " "
            else:                       # 나머지 부분은 시작점과 num을 알맞게 바꿔 다시 함수를 호출한다.
                solution(nx, ny, num-1)


N = int(input())
k = 1

while True:             # math.log로 값을 계산할 경우 오차가 발생하므로 직접 계산해준다.
    if 3 ** k == N:
        break
    else:
        k += 1

board = [["*" for _ in range(N)] for _ in range(N)]
solution(0, 0, k)

for a in range(N):
    sys.stdout.write("".join(board[a]) + "\n")
