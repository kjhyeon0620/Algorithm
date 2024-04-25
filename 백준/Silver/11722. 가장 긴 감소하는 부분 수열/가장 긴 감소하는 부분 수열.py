N = int(input())
A = list(map(int, input().split()))
memo = [1 for _ in range(N)]

for i in range(1, N):           # i 번째까지 가장 긴 감소하는 부분 수열의 크기를 저장한다.
    for j in range(i):
        if A[i] < A[j]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))
