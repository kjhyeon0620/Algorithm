N = int(input())
nums = list(map(int, input().split()))
memo = [1 for _ in range(N)]
for i in range(N-2, -1, -1):
    for j in range(i, N):
        if nums[j] > nums[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))