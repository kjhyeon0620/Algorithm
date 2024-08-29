N = int(input())
An = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
dc = dict()

for a in An:
    dc[a] = 1

for n in nums:
    if dc.get(n) is None:
        print(0)
    else:
        print(1)