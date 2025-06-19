import heapq
import math
from collections import deque
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

distance = [math.inf] * (V+1)
distance[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

heap = [(0, K)]
while heap:
    dist, node = heapq.heappop(heap)
    if dist > distance[node]:
        continue
    for neighbor, weight in graph[node]:
        new_dist = dist + weight
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(heap, (new_dist, neighbor))

for i in range(1, V+1):
    if math.isinf(distance[i]):
        sys.stdout.write("INF\n")
    else:
        sys.stdout.write(str(distance[i]) + "\n")