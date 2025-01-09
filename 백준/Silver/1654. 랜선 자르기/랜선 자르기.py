K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]
left, right = 1, max(lans)
ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)