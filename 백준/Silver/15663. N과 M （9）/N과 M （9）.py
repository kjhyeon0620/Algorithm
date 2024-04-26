import sys


N, M, = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []
visited = [False for _ in range(N)]


def dfs():
    if len(stack) == M:
        sys.stdout.write(" ".join(map(str, stack)) + "\n")
        return
    prev = 0
    for i in range(N):
        if not visited[i] and arr[i] != prev:
            visited[i] = True
            stack.append(arr[i])
            prev = arr[i]
            dfs()
            visited[i] = False
            stack.pop()

dfs()
