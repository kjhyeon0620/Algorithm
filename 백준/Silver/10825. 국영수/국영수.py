# sort 와 lambda를 이용해 정렬한다.

import sys


input = sys.stdin.readline
info = []
N = int(input())

for _ in range(N):
    info.append(list(input().split()))

info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in info:
    sys.stdout.write(student[0] + "\n")

