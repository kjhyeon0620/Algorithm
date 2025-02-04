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
        tmp = A[0]
        for i in range(N-1):
            tmp = calculator(tmp, A[i+1], stack[i])
        ans.append(tmp)
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


ans = []
dfs()

print(max(ans))
print(min(ans))