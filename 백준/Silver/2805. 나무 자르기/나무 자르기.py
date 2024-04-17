# 이분탐색으로 정답을 구한다.

N, M = map(int, input().split())
heights = list(map(int, input().split()))
left, right = 1, max(heights)
while left <= right:
    total = 0
    mid = (left + right) // 2
    for height in heights:
        if height <= mid:
            continue
        total += height - mid
    if total > M:
        left = mid+1
    elif total < M:
        right = mid-1
    else:
        print(mid)
        exit(0)
print(right)