import heapq
import math
import sys

input = sys.stdin.readline

# 노드와 간선의 개수
N = int(input())
M = int(input())

# 그래프 초기화
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    graph[s].append([e, v])

# 시작점과 끝점 입력
start, end = map(int, input().split())

# 방문 여부와 비용 초기화
visited = [False for _ in range(N+1)]
cost = [math.inf for _ in range(N+1)]
cost[start] = 0

# 다익스트라 알고리즘을 위한 우선순위 큐
hq = [[0, start]]  # (현재 비용, 노드)
heapq.heapify(hq)

# 다익스트라 알고리즘
while hq:
    current_cost, node = heapq.heappop(hq)
    
    if visited[node]:
        continue
    
    visited[node] = True

    # 인접한 노드 탐색
    for neighbor, weight in graph[node]:
        new_cost = current_cost + weight
        if new_cost < cost[neighbor]:
            cost[neighbor] = new_cost
            heapq.heappush(hq, [new_cost, neighbor])

# 끝점까지의 최소 비용 출력
print(cost[end])
