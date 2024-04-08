# 대칭 차집합의 개수는 n(A) + n(B) - 2 * n(A, B의 교집합) 이다

nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(nA + nB - (2 * len(A.intersection(B))))