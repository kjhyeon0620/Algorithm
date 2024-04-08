# dictionary를 이용해 데이터를 저장한다.

import sys


input = sys.stdin.readline
N, M = map(int, input().split())
names = dict()
nums = dict()

for i in range(1, N+1):
    inp = input().strip()
    names[inp] = i
    nums[i] = inp

for _ in range(M):
    question = input().strip()
    
    if question.isalpha():
        print(names[question])
    else:
        print(nums[int(question)])
