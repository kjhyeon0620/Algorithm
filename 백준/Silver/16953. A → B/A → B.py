# 일의 자리 수로 구분하여 뒤에서부터 역으로 계산한다.
# 일의 자리 3,5,7,9 -> 더 이상 연산 x
# 일의 자리 1 -> 1을 뺀다
# 일의 자리 0,2,4,6,8 -> 2로 나눈다.

A, B = map(int, input().split())
cnt = 0

while A < B:
    num = B % 10
    if num % 2 == 0:
        B //= 2
        cnt += 1
    elif num == 1:
        B //= 10
        cnt += 1
    else:
        break
        
if A == B:
    print(cnt+1)
else:
    print(-1)
