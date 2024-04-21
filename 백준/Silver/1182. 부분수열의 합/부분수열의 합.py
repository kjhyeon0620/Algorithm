N, S = map(int, input().split())

stack = []
nums = list(map(int, input().split()))
cnt = 0


def dfs(start, m):
    global cnt
    if len(stack) == m:
        total = 0
        for el in stack:
            total += el
        if total == S:
            cnt += 1
        return
    for i in range(start, N):
        stack.append(nums[i])
        dfs(i+1, m)
        stack.pop()


for i in range(1, N+1):
    dfs(0, i)
print(cnt)