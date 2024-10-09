N, M = map(int, input().split())
board = [input() for _ in range(N)]

ans = [1]
dx = [0, 1, 1]
dy = [1, 0, 1]

for i in range(N-1):
    for j in range(M-1):
        length = 1
        while True:
            if i+length > N-1 or j+length > M-1:
                break
            for d in range(3):
                if board[i][j] != board[i+dy[d]*length][j+dx[d]*length]:
                    break
            else:
                ans.append((length+1) ** 2)
            length += 1
            
print(max(ans))