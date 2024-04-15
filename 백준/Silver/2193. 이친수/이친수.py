# 앞에서 0이 나왔을 때, i자리 이친수의 개수를 저장한다.
# 시작은 10으로 고정되므로 f(N-2)가 정답이다.

N = int(input())
if N == 1 or N == 2:
    print(1)
else:
    memo = [-1] * N
    memo[1] = 2
    memo[2] = 3
    for i in range(3, N-1):
        memo[i] = memo[i-1] + memo[i-2]
    print(memo[N-2])
