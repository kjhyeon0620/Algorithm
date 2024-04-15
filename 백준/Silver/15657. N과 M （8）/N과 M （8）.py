# 백트래킹을 이용해 해결한다.

import sys


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
stack = []


def dfs(start):
    if len(stack) == M:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
        return
    for i in range(start, N):
        stack.append(nums[i])
        dfs(i)
        stack.pop()


dfs(0)
