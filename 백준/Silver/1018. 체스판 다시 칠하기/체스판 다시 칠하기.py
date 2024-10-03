def findMin(startX, startY, b):
    cnt = 0
    for x in range(8):
        for y in range(8):
            if (x+y) % 2 == 0 and b[startY+y][startX+x] != "B":
                cnt += 1
            if (x+y) % 2 == 1 and b[startY+y][startX+x] != "W":
                cnt += 1
    return min(cnt, 64-cnt)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

ans = []

for i in range(M-8+1):
    for j in range(N-8+1):
        ans.append(findMin(i, j, board))

print(min(ans))