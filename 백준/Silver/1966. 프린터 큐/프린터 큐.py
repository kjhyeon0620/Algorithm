import heapq
from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque([i for i in range(N)])
    ans = 1
    maxHeap = [-p for p in priority]
    heapq.heapify(maxHeap)
    while True:
        if priority[queue[0]] == -maxHeap[0]:
            if queue.popleft() == M:
                print(ans)
                break
            else:
                heapq.heappop(maxHeap)
                ans += 1
        else:
            queue.append(queue.popleft())
