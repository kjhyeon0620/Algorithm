N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort(reverse=True)
left, right = 0, trees[0]

while left <= right:
    total = 0
    mid = (left + right) // 2
    for height in trees:
        if height <= mid:
            break
        total += height - mid
    if total == M:
        right = mid
        break
    elif total < M:
        right = mid - 1
    else:
        left = mid + 1

print(right)