N = int(input())
heights = list(map(int, input().split()))
ans = [0] * N
stack = []

for i in range(N):
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] + 1  # 수신 가능한 탑의 번호 (1-based)
    stack.append(i)

print(*ans)
