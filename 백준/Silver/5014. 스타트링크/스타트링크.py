# dp를 이용해 목표 층에서부터 내려오면서 현재 층까지 가기 위한 최솟값을 구한다.

F, S, G, U, D = map(int, input().split())
memo = [-1] * (F+1)
memo[G] = 0
stack = [G]

while stack:
    floor = stack.pop()
    if floor + D <= F and (memo[floor+D] == -1 or memo[floor+D] > memo[floor] + 1):
        memo[floor+D] = memo[floor] + 1
        stack.append(floor+D)
    if floor-U > 0 and (memo[floor-U] == -1 or memo[floor-U] > memo[floor] + 1):
        memo[floor-U] = memo[floor] + 1
        stack.append(floor-U)

if memo[S] == -1:
    print("use the stairs")
else:
    print(memo[S])