# dp를 이용하여 최댓값을 저장해나간다.

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [P[1]] * (N+1)

for i in range(2, N+1):
    tmp = [P[i]]
    for j in range(1, i // 2 + 1):
        tmp.append(dp[j] + dp[i-j])

    dp[i] = max(tmp)

print(dp[N])