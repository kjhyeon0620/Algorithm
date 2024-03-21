# 1. 분해합을 구하는 함수를 만든다.
# 2. 1부터 N-1 까지 분해합을 구하여 N이 되는 수가 있다면 출력한다.

def solution(num):
    res = num
    while num != 0:
        res += num % 10
        num = num // 10
    return res


N = int(input())
ans = 0

for i in range(1, N):
    if solution(i) == N:
        ans = i
        break
        
print(ans)