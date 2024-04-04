# for 문을 이용하여 행렬의 곱셈을 구현한다.

N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

for _ in range(M):
    B.append(list(map(int, input().split())))

ans = [[] for _ in range(N)]

for i in range(N):
    for j in range(K):
        tmp = 0
        for k in range(M):
            tmp += A[i][k] * B[k][j]
        ans[i].append(tmp)

for i in range(N):
    print(*ans[i])