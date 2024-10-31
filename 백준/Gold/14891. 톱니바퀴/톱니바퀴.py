from collections import deque


def operation(op, wheel):
    if op == 1:
        wheel.appendleft(wheel.pop())
        return wheel
    else:
        wheel.append(wheel.popleft())
        return wheel


wheels = [deque(list(input())) for _ in range(4)]

for _ in range(int(input())):
    queue = deque()
    n, o = map(int, input().split())
    queue.append([n-1, o])
    isTurned = [False for _ in range(4)]
    
    while queue:
        num, opCode = queue.popleft()
        isTurned[num] = True
        if 0 <= num-1 and not isTurned[num-1] and wheels[num][6] != wheels[num-1][2]:
            isTurned[num-1] = True
            queue.append([num-1, -opCode])
        if 3 >= num+1 and not isTurned[num+1] and wheels[num][2] != wheels[num+1][6]:
            isTurned[num+1] = True
            queue.append([num+1, -opCode])
        operation(opCode, wheels[num])
        
ans = 0

for i in range(4):
    if wheels[i][0] == '1':
        ans += 2**i

print(ans)
