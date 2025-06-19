import math
import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

# 거리 배열 초기화
distance = [math.inf] * (V+1)
distance[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 우선순위 큐(힙) 사용
heap = [(0, K)]  # (거리, 노드)
while heap:
    dist, node = heapq.heappop(heap)
    if dist > distance[node]:
        continue  # 이미 더 짧은 거리로 방문한 경우 무시
    for neighbor, weight in graph[node]:
        new_dist = dist + weight
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(heap, (new_dist, neighbor))

# 결과 출력
for i in range(1, V+1):
    print("INF" if math.isinf(distance[i]) else distance[i])
