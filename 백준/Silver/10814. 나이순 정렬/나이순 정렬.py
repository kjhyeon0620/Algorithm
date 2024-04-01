# 가입 순서, 나이, 이름을 모두 리스트에 저장한 후 sort를 이용해 정렬한다.

import sys


input = sys.stdin.readline
N = int(input())
members = []
for i in range(N):
    age, name = input().split()
    members.append([age, name, i])

members.sort(key=lambda m: (int(m[0])))

for member in members:
    sys.stdout.write(f'{member[0]} {member[1]}\n')
