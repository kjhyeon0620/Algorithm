N = int(input())
schedule = [0] + [list(map(int, input().split())) for _ in range(N)]
memo = [0 for _ in range(N+2)]
for i in range(N, 0, -1):
    t, p = schedule[i]
    if i + t <= N+1:
        memo[i] = max(memo[i+1], p+memo[i+t])
    else:
        memo[i] = memo[i+1]

print(memo[1])

