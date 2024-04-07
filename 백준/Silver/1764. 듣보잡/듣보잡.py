# dictionary 에 듣도 못한 사람을 저장한다
# 보도 못한 사람을 dictionary에 검색해서 존재하면 ans에 넣는다

import sys


input = sys.stdin.readline
N, M = map(int, input().split())
names = dict()
ans = []
cnt = 0
for _ in range(N):
    names[input().strip()] = 1

for _ in range(M):
    inp = input().strip()
    if names.get(inp) is not None:
        ans.append(inp)
        cnt += 1

ans.sort()
print(cnt)
for name in ans:
    print(name)
