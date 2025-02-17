N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))
ans = 0
end = -1

for i in range(N):
    if meetings[i][0] >= end:
        end = meetings[i][1]
        ans += 1

print(ans)