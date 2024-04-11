# 백트래킹으로 푼다. 수열이 오름차순이 되게 하기 위해 dfs의 인자로 start 설정한다.
# start를 설정해주면 중복이 방지되기 때문에 visited는 생략한다.

import sys


def dfs(start):
    if len(stack) == M:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
        return
    for i in range(start, N+1):
        stack.append(i)
        dfs(i+1)
        stack.pop()


N, M = map(int, input().split())
stack = []
dfs(1)
