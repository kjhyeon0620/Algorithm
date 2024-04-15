# 수열을 정렬한 후 백트래킹을 이용해 출력한다.

import sys


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N
stack = []


def dfs():
    if len(stack) == M:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
        return

    for i in range(N):
        if not visited[i]:
            stack.append(nums[i])
            visited[i] = True
            dfs()
            stack.pop()
            visited[i] = False


dfs()
