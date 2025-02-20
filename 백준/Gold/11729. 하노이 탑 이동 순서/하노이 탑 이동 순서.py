import sys


def solution(now, tmp, des, length):
    global cnt
    if length == 1:
        cnt += 1
        ans.append((now, des))
        return
    solution(now, des, tmp, length-1)
    cnt += 1
    ans.append((now, des))
    solution(tmp, now, des, length-1)


cnt = 0
ans = []
solution(1, 2, 3, int(input()))
print(cnt)
for el in ans:
    sys.stdout.write(str(el[0]) + ' ' + str(el[1]) + '\n')
    