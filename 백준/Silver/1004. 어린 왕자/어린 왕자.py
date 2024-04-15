# 출발점과 도착점 중 한 점만 원 안에 들어가 있을 때 해당 원의 경계를 반드시 지나간다.

import sys


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        d1 = (planets[i][0] - x1) ** 2 + (planets[i][1] - y1) ** 2
        d2 = (planets[i][0] - x2) ** 2 + (planets[i][1] - y2) ** 2
        
        if d1 > planets[i][2] ** 2 > d2:
            cnt += 1
        elif d1 < planets[i][2] ** 2 < d2:
            cnt += 1
    print(cnt)
