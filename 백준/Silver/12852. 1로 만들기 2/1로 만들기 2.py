# dp에 연산의 최솟값과 포함되어 있는 수를 같이 저장해둔다.
# dp[num][0] 의 0번째 인덱스는 연산의 최솟값이고,
# 1번째 인덱스부터 마지막 인덱스까지는 포함되어 있는 수를 1부터 차례대로 나열한다.


N = int(input())
dp = [[] for _ in range(N+1)]
dp[1].append([0, 1])
if N >= 2:
    dp[2].append([1, 1, 2])
if N >= 3:
    dp[3].append([1, 1, 3])


for i in range(4, N+1):
    tmp = [dp[i-1][0]]
    if i % 2 == 0:
        tmp.append(dp[i//2][0])
    if i % 3 == 0:
        tmp.append(dp[i//3][0])
    tmp.sort()
    tmp_copy = tmp[0].copy()
    tmp_copy[0] += 1
    tmp_copy.append(i)
    dp[i].append(tmp_copy)

print(dp[N][0][0])
for i in range(dp[N][0][0] + 1, 0, -1):
    print(dp[N][0][i], end=" ")
