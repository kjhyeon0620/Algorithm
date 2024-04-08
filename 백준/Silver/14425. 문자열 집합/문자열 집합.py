# dictionary를 이용해 개수를 센다.

import sys


input = sys.stdin.readline

N, M = map(int, input().split())
S = dict()
ans = 0

for _ in range(N):
    inp = input().strip()
    S[inp] = True
    
for _ in range(M):
    findStr = input().strip()
    if S.get(findStr) is not None:
        ans += 1
        
print(ans)
