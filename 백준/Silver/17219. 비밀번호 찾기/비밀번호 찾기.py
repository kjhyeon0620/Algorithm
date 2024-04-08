# dictionary를 이용해 비밀 번호를 저장한다

import sys


input = sys.stdin.readline
N, M, = map(int, input().split())
passwords = dict()

for _ in range(N):
    url, password = input().split()
    passwords[url] = password
    
for _ in range(M):
    sys.stdout.write(passwords[input().rstrip()] + "\n")