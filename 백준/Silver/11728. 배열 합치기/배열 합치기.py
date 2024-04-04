# A와 B의 원소들을 포인터를 이용해 하나씩 비교해가며 새로운 배열에 추가한다.

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ptrA, ptrB = 0, 0
ans = []

while True:
    if ptrA > N - 1:
        for i in range(ptrB, M):
            ans.append(B[i])
        break

    if ptrB > M - 1:
        for i in range(ptrA, N):
            ans.append(A[i])
        break

    if A[ptrA] == B[ptrB]:
        ans.append(A[ptrA])
        ans.append(B[ptrB])
        ptrA, ptrB = ptrA+1, ptrB+1

    elif A[ptrA] < B[ptrB]:
        ans.append(A[ptrA])
        ptrA += 1

    else:
        ans.append(B[ptrB])
        ptrB += 1

print(*ans)