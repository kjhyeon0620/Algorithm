# 해당 칸의 인덱스를 i,j 라고 했을 때, i+j가 홀수 / 짝수인 경우로 나누어서 색이 맞는지 확인하면 된다.

N, M = map(int, input().split())

board = [input() for _ in range(N)]
evenW = ["W", "B"]  # 왼쪽 위 첫 번째 칸이 "W"인 경우
oddW = ["B", "W"]   # 왼쪽 위 첫 번째 칸이 "B"인 경우

min_cnt = 32
for i in range(N-7):
    for j in range(M-7):
        checkList = evenW if evenW[(i + j) % 2] == board[i][j] else oddW    # evenW와 oddW중 해당하는 체크리스트를 고른다
        cnt = 0
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y] != checkList[(i+x+j+y) % 2]:
                    cnt += 1
        min_cnt = min(cnt, min_cnt, 64-cnt) # 바꿔야 하는 칸이 32를 넘어갈 경우는 위에서 결정한 체크리스트와 반대로 했을 때 
                                            # 최소가 되는 것이기에 64에서 cnt를 빼준 것도 최솟값으로 고려해준다.

print(min_cnt)