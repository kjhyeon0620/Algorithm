import sys


input = sys.stdin.readline

N, M, = map(int, input().split())

notHear = set()
ans = []

for _ in range(N):
    notHear.add(input())

for _ in range(M):
    notLook = input()
    if notLook in notHear:
        ans.append(notLook.rstrip())

print(len(ans))
for both in sorted(ans):
    print(both)