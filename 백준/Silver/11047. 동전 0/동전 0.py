N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]
ans = 0
idx = N-1
while K:
    ans += K // values[idx]
    K %= values[idx]
    idx -= 1
print(ans)