# 리스트에 값을 저장한 후 오름차순으로 정렬한다.
# 각 값을 돌며 해당 값을 최솟값으로 하여 물체를 들었을 때 들 수 있는 중량을 확인하고 최댓값을 저장한다.

import sys


input = sys.stdin.readline
N = int(input())
weights = [int(input()) for _ in range(N)]
weights.sort()
maxWeight = -1

for i in range(N):
    maxWeight = max(maxWeight, weights[i] * (N-i))
    
print(maxWeight) 