N = int(input())
heights = list(map(int, input().split()))
ans = [0 for _ in range(N)]
stack = []
for i in range(N-1, -1, -1):
    for j in range(len(stack)):
        idx, height = stack.pop()
        if height <= heights[i]:
            ans[idx] = i+1
        else:
            stack.append([idx, height])
            break
    stack.append([i, heights[i]])

print(*ans)