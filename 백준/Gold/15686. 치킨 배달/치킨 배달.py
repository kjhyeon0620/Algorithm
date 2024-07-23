# 치킨집 중 M 개를 고를 수 있는 모든 경우의 수에 대해서 치킨 거리를 계산한 후 최솟값을 출력한다.

import itertools


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chickens = []   # 모든 치킨집을 찾는다.
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append([i, j])

res = []
for remain in itertools.combinations(chickens, M): # 모든 경우의 수에 대해서
    tmp = 0
    for a in range(N):  # 도시의 치킨 거리를 구한다.
        for b in range(N):
            if city[a][b] == 1:
                minVal = 1000
                for pos in remain:
                    minVal = min(minVal, (abs(a - pos[0]) + abs(b - pos[1])))
                tmp += minVal
    res.append(tmp)

print(min(res))
