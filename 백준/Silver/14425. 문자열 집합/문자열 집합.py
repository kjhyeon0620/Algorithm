# dictionary를 이용해 개수를 센다.

import sys


input = sys.stdin.readline

N, M = map(int, input().split())
S = dict()
ans = 0

for _ in range(N):
    inp = input()
    S[inp] = True
    
for _ in range(M):
    findStr = input()
    if findStr in S:
        ans += 1
        
print(ans)
