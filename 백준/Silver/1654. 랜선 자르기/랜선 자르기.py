# 이분탐색으로 해결한다.

import sys


input = sys.stdin.readline
K, N = map(int, input().split())
lengths = [int(input()) for _ in range(K)]
left, right = 1, max(lengths)
while left <= right:
    mid = (left + right) // 2
    total = 0
    for length in lengths:
        total += length // mid
    if total >= N:
        left = mid + 1
    elif total < N:
        right = mid - 1
print(right)