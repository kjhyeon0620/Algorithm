# enter 한 사람들을 dictionary에 저장하고, leave한 사람들은 dictionary에서 삭제한다.
# 로그에 기록된 수행이 끝나면 dictionary에 남아있는 key들을 list로 변환한 후 역순으로 정렬한다.

import sys


input = sys.stdin.readline
n = int(input())
exists = dict()

for _ in range(n):
    name, op = input().split()
    if op == "enter":
        exists[name] = True
    else:
        exists.pop(name)

ans = list(exists.keys())
ans.sort(reverse=True)

for el in ans:
    sys.stdout.write(el + "\n")



