# itertools 라이브러리를 사용해 최댓값을 구한다.

import itertools


N = int(input())
A = list(map(int, input().split()))
ans = []
for el in itertools.permutations(A, N):
    total = 0
    for i in range(N-1):
        total += abs(el[i+1] - el[i])
    ans.append(total)

print(max(ans))