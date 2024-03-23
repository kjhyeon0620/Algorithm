# 리스트에 바구니의 순서를 저장한 후, 주어진 범위만큼 역순으로 저장한다.

N, M = map(int, input().split())
baskets = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    while i < j:
        baskets[i], baskets[j] = baskets[j], baskets[i]
        i += 1
        j -= 1

print(*baskets[1:])