# 크기가 8x8밖에 되지 않으므로, 단순하게 2중 for 문으로 해결한다.
# 0,0 / 0,2 / 0,4 / 0,6 / 1,1 -> x와 y의 합이 짝수일 경우에만 흰색 칸이다.

board = []
cnt = 0

for _ in range(8):
    board.append(input())

for x in range(8):
    for y in range(8):
        if not (x+y) % 2 and board[y][x] == "F":
            cnt += 1

print(cnt)