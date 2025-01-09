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
            sys.stdout.write(str(heapq.heappop(minHeap)) + "\n")

    else:
        heapq.heappush(minHeap, x)
