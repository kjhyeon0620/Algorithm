# 왼쪽과 오른쪽 중 가까운 곳으로 이동시키고, 횟수를 센다

from collections import deque


N, M = map(int, input().split())
findNums = list(map(int, input().split()))
queue = list(range(1, N+1))
cnt = 0
length = N

for num in findNums:
    idx = queue.index(num)
    queue = queue[idx+1:] + queue[:idx]
    cnt += min(idx, length-idx)
    length -= 1

print(cnt)