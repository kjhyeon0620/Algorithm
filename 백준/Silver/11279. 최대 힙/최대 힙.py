# 최소 힙에 수를 음수로 변환하여 집어넣는다.
import heapq
import sys


input = sys.stdin.readline
N = int(input())
h = []
cnt = 0

for _ in range(N):
    x = int(input())
    if x == 0:
        if cnt == 0:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(-heapq.heappop(h)) + "\n")
            cnt -= 1
    else:
        heapq.heappush(h, -x)
        cnt += 1
