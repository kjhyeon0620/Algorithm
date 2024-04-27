# "해당 지점에서 출발했을 때 얻을 수 있는 최댓값"을 저장하는 리스트를 만든다.
# dp를 이용해 도착점부터 출발점까지 역순으로 위를 구하여 정답을 구한다.

N, M = map(int, input().split())
dp = [[-1 for _ in range(M)] for _ in range(N)]
maze = []

for _ in range(N):
    maze.append(list(map(int, input().split())))

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        tmp = [0]
        if i+1 <= N-1:
            tmp.append(dp[i+1][j])
        if j+1 <= M-1:
            tmp.append(dp[i][j+1])
        elif i+1 <= N-1 and j+1 <= M-1:
            tmp.append(dp[i+1][j+1])
        dp[i][j] = maze[i][j] + max(tmp)
        
print(dp[0][0])
