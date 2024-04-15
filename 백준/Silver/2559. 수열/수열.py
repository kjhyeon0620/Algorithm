# 연속적인 합을 저장한 후 최댓값을 구한다

N, K = map(int, input().split())
nums = list(map(int, input().split()))
memo = [0] * (N-K+1)
memo[0] = sum(nums[:K])

for i in range(1, N-K+1):
    memo[i] = memo[i-1] - nums[i-1] + nums[i+K-1]
    
print(max(memo))
