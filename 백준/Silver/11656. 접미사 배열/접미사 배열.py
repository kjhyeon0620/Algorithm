# 모든 접미사들을 리스트에 저장한 후 정렬한다.

import sys


S = input()
length = len(S)
arr = []
for i in range(length):
    arr.append(S[i:])
arr.sort()
for el in arr:
    sys.stdout.write(el + "\n")
