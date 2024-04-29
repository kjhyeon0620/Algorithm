# dp에 해당 N부터 해당 위치까지 도달하는데 걸리는 최소 시간을 저장한다.

N, K = map(int, input().split())
dp = [-1 for _ in range(K+2)]

if N >= K:
    print(N-K)

else:
    for i in range(K+2):
        if i <= N:          # 뒤로는 1씩만 갈 수 있으므로 뒤에 있다면 위치만큼의 시간이 걸린다.
            dp[i] = N - i
        elif i % 2 == 0:    # 짝수인 경우 이전 dp와 2로 나눈 위치의 dp를 비교해서 저장한다.
            dp[i] = min(dp[i-1], dp[i//2]) + 1  # 다음 dp를 고려해주지 않았으므로
            dp[i-1] = min(dp[i-1], dp[i]+1)     # 이전 dp까지 고려해준다.
        else:
            dp[i] = dp[i-1]+1

    print(dp[K])

