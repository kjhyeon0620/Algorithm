# dfs로 촌수를 계산한다.

import sys


def dfs(start, cnt):        # dfs 함수에 cnt 변수를 인자로 설정해 횟수를 센다.
    if visited[start]:
        return
    if start == find2:      # 답을 찾았을 경우 exit로 실행을 종료한다.
        print(cnt)
        exit(0)
    visited[start] = True
    for el in graph[start]:
        if not visited[el]:
            dfs(el, cnt+1)

input = sys.stdin.readline
n = int(input())
find1, find2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
stack = []
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(find1, 0)

print(-1)       # 실행이 종료되지 않았다는건 촌수를 계산할 수 없다는 것이므로 -1을 출력한다.
