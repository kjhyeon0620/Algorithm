nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

cnt = 0

for el in A:
    if el in B:
        cnt += 1

print(nA + nB - 2 * cnt)
