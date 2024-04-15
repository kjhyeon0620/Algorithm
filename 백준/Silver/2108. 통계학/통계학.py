import sys


input = sys.stdin.readline
memo = [0] * 8001
lst = []
N = int(input())

for _ in range(N):
    num = int(input())
    memo[num+4000] += 1
    lst.append(num)
    
lst.sort()
print(round(sum(lst) / N))
print(lst[N//2])

_max = max(memo)
if memo.count(_max) == 1:
    print(memo.index(_max)-4000)
else:
    for i in range(memo.index(_max)+1, 8001):
        if memo[i] == _max:
            print(i-4000)
            break
            
print(lst[N-1] - lst[0])
