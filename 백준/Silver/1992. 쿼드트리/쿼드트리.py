# 주어진 구간이 모두 하나의 수로 되어있지 않다면 4개로 분할하여 각각 연산한고, 이를 반복한다.

N = int(input())
board = []
for _ in range(N):
    board.append(input())

d = [[0, 0], [0, 1], [1, 0], [1, 1]]


def solution(x, y, n):
    tmp = ""
    first = board[x][y]
    for i in range(n):
        for j in range(n):
            if board[x+i][y+j] != first:    # 해당 구간에서 다른 부분이 있다면
                n //= 2
                tmp += "("                  # (를 추가하고, 
                for k in range(4):          # 4개의 구간에 대해 함수를 실행한 후 값을 저장한다.
                    tmp += solution(x + n * d[k][0], y + n * d[k][1], n)
                tmp += ")"                  # 4개의 구간에 대한 연산을 마친 후, )를 추가한다.
                return tmp
    return first                            # 모두 동일한 숫자를 가지고 있다면 해당 숫자를 반환한다.


print(solution(0, 0, N))
