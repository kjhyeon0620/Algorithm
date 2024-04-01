import sys


input = sys.stdin.readline
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

points.sort(key=lambda x: (x[1], x[0]))

for point in points:
    sys.stdout.write(f'{point[0]} {point[1]}\n')