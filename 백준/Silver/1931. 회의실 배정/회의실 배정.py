# 끝나는 시간을 기준으로 정렬한다.
# 끝나는 시간이 가장 빠른 회의부터 그 다음 회의가 가능한 빠른 회의를 찾는다.
# 위를 마지막까지 반복한다.

import sys


input = sys.stdin.readline
N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))
ans = 0
tmp = -1
for i in range(N):
    if tmp <= times[i][0]:
        ans += 1
        tmp = times[i][1]

print(ans)