# heapq에 2개의 값(절댓값과 원래의 값)을 저장하여 절댓값을 기준으로 정렬하고, 값은 값이 있다면 원래의 값까지 비교한다.

import heapq as hq
import sys


input = sys.stdin.readline
N = int(input())

length = 0
heap = []

for _ in range(N):
    x = int(input())
    if x:
        hq.heappush(heap, [abs(x), x])
        length += 1
    else:
        if length:
            print(hq.heappop(heap)[1])
            length -= 1
        else:
            print(0)

