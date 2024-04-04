# 2차원 리스트에 수를 입력받은 후 주어진 범위에 맞춰 수를 더한 후 출력한다.
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    i, j, x, y = i-1, j-1, x-1, y-1
    total = 0
    
    for el in range(i, x+1):
        total += sum(lst[el][j:y+1])
        
    print(total)


