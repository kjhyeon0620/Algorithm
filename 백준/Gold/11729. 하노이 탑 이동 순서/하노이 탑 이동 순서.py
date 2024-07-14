import sys


def solution(now, tmp, goal, num):
    if num == 1:
        ans.append([now, goal])
    else:
        solution(now, goal, tmp, num-1)
        solution(now, tmp, goal, 1)
        solution(tmp, now, goal, num-1)


K = int(input())
ans = []
solution(1, 2, 3, K)
print(len(ans))
for process in ans:
    sys.stdout.write(str(process[0]) + " " + str(process[1]) + "\n")