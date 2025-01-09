import heapq
import sys


input = sys.stdin.readline
N = int(input())

minHeap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(minHeap) == 0:
            print(0)
        else:
            print(heapq.heappop(minHeap))

    else:
        heapq.heappush(minHeap, x)
