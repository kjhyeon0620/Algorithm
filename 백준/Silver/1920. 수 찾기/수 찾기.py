# dictionary를 이용해 존재하는 지 판단한다.

import sys


input = sys.stdin.readline
N = int(input())
isExist = dict()

for getNum in map(int, input().split()):
    isExist[getNum] = 1

M = int(input())
for findNum in map(int, input().split()):
    if isExist.get(findNum) is None:
        sys.stdout.write("0\n")
    else:
        sys.stdout.write("1\n")




