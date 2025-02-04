# + - * /

N = int(input())
A = list(map(int, input().split()))
numOfOperators = list(map(int, input().split()))
stack = []
nums = []
ops = []
visited = [False for _ in range(N-1)]
for i in range(4):
    for j in range(numOfOperators[i]):
        nums.append(i)


def dfs():
    if len(stack) == N-1:
        ops.append(stack.copy())
        return
    for i in range(N-1):
        if not visited[i]:
            visited[i] = True
            stack.append(nums[i])
            dfs()
            visited[i] = False
            stack.pop()


def calculator(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


dfs()
ans = []

for op in ops:
    tmp = A[0]
    for i in range(N-1):
        tmp = calculator(tmp, A[i+1], op[i])
    ans.append(tmp)

print(max(ans))
print(min(ans))