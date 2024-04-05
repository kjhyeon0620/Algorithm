# stack의 pop을 이용하여 문제를 해결한다.

import sys


input = sys.stdin.readline
K = int(input())
stack = []
total = 0
for _ in range(K):
    num = int(input())
    if num == 0:
        total -= stack.pop()
    else:
        stack.append(num)
        total += num

print(total)
