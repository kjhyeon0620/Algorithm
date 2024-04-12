# n번째 인덱스 까지의 합을 리스트에 저장해둔 후 이를 이용해 해결한다.
# ex) 1~3 합 : s(3) - s(0)
# n ~ k 합 : s(k) - s(n-1)
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
sums = [0] * (N+1)
sums[1] = nums[1]

for i in range(2, N+1):
    sums[i] = sums[i-1] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])


