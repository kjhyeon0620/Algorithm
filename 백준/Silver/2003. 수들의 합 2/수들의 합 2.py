N, M = map(int, input().split())
A = list(map(int, input().split()))

left, right = 0, 1
total = A[0]
cnt = 0

while True:
    if total == M:
        cnt += 1
        total -= A[left]
        left += 1
    elif total > M:
        total -= A[left]
        left += 1
    else:
        if right == N:
            break
        total += A[right]
        right += 1

print(cnt)
