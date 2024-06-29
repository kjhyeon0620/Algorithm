# 자릿수 별로 계산한다.

N = int(input())
memo = [[-1] * 10 for _ in range(N+1)] # memo[n][k] => n번째 자리수가 k일 때 오르막 수의 개수

for a in range(10):     # 한 자리 수는 따로 계산
    memo[1][a] = 10 - a

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            memo[i][j] = 0
            for k in range(10):
                memo[i][j] += memo[i-1][k]
            memo[i][j] %= 10007
        else:
            memo[i][j] = memo[i][j-1] - memo[i-1][j-1]
            memo[i][j] %= 10007

print(memo[N][0])