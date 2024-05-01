# 아래에서부터 첫 째 줄까지 최댓값을 차례대로 저장한다.

import sys


input = sys.stdin.readline
n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(i+1):
        triangle[i][j] = max(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]

print(triangle[0][0])