N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]


def check(x, y, cnt):
    color = board[x][y]

    for i in range(cnt):
        for j in range(cnt):
            if board[x+i][y+j] != color:
                cnt //= 2
                for dx in range(2):
                    for dy in range(2):
                        check(x+(dx*cnt), y+(dy*cnt), cnt)
                return

    ans[color] += 1


check(0, 0, N)

for i in range(2):
    print(ans[i])
