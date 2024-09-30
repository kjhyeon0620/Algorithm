import sys


N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
findNums = list(map(int, input().split()))

for fn in findNums:
    if fn in A:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
