# 큰 수와 작은 수 끼리 곱하면 최소가 된다.
# A, B 모두 재배열 해도 조건을 만족한다.
# A는 오름차순, B는 내림차순으로 정렬한 후 각 위치별로 곱해서 더한다.

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

ans = 0
for i in range(N):
    ans += A[i] * B[i]
print(ans)
