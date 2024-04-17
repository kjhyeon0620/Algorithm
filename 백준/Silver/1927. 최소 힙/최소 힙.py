# heapq를 이용해 해결한다.

import heapq
import sys


input = sys.stdin.readline
heap = []
cnt = 0
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if cnt == 0:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(heapq.heappop(heap)) + "\n")
            cnt -= 1
    else:
        heapq.heappush(heap, x)
        cnt += 1
