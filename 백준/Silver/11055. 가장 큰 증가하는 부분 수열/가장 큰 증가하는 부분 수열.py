N = int(input())
A = list(map(int, input().split()))
memo = A.copy()

for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[i] < A[j]:
            memo[i] = max(memo[i], memo[j] + A[i])

print(max(memo))