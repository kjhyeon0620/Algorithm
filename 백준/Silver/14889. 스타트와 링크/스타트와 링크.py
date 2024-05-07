import itertools
import sys


input = sys.stdin.readline
N = int(input())
status = []

for _ in range(N):
    status.append(list(map(int, input().split())))

teamA = list(itertools.combinations(range(N), N//2))
ans = []

for i in range(len(teamA)//2):
    totalA = 0
    totalB = 0
    teamB = []
    for j in range(N):
        if j not in teamA[i]:
            teamB.append(j)
    for k in range(N//2):
        for l in range(N//2):
            totalA += status[teamA[i][k]][teamA[i][l]]
            totalB += status[teamB[k]][teamB[l]]
    ans.append(abs(totalA - totalB))

print(min(ans))


