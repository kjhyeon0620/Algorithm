# 스택을 이용한다

import sys


input = sys.stdin.readline
n = int(input())
tmp = 0
ans = []
stack = []
for _ in range(n):
    num = int(input())
    if num > tmp:
        for i in range(tmp+1, num):
            stack.append(i)
            ans.append("+")
        ans.append("+") # num은 push한 후 바로 pop
        ans.append("-")
        tmp = num
    else:
        if stack.pop() != num:
            ans = ["NO"]
            break
        else:
            ans.append("-")

sys.stdout.write("\n".join(ans))
