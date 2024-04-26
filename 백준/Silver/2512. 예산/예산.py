# 분할 탐색으로 답을 구한다.

N = int(input())
requests = sorted(list(map(int, input().split())))
M = int(input())

left, right = 1, requests[-1]

while left <= right:
    mid = (left + right) // 2
    total = 0
    for req in requests:
        if req > mid:
            total += mid
        else:
            total += req
    if total == M:
        right = mid
        break
    elif total > M:
        right = mid - 1
    else:
        left = mid + 1

print(right)