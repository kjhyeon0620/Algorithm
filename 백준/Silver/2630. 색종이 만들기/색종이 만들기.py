import sys


def check(x, y, k):
    val = board[y][x]
    global cntBlue
    global cntWhite

    for i in range(k):
        for j in range(k):
            if board[y+i][x+j] != val:  # 처음 색깔과 다른 색깔이 발견되면 즉시 False
                return False

    for i in range(k):                  # 모두 같은 색깔이므로 visited에 체크해줌
        for j in range(k):
            visited[y+i][x+j] = True
    if val == 1:                        # 색깔에 맞게 count 증가
        cntBlue += 1
    else:
        cntWhite += 1

    return True


input = sys.stdin.readline
N = int(input())
board = []
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))
tmp = N
cntWhite = 0
cntBlue = 0
while True:
    if tmp == 0:
        break
    for i in range(0, N, tmp):      # 쪼개는 크기에 맞게 모든 위치를 check 함수로 검사시킴
        for j in range(0, N, tmp):
            if not visited[j][i]:
                check(i, j, tmp)

    tmp //= 2

print(cntWhite)
print(cntBlue)
