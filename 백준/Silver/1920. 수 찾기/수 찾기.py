N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
findNums = list(map(int, input().split()))

for fn in findNums:
    if fn in A:
        print(1)
    else:
        print(0)
