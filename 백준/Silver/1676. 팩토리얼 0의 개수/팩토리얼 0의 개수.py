# 입력받은 수의 팩토리얼을 구한 후 %10을 이용해 연속하는 0의 개수를 구한다.

N = int(input())
facto = 1

for i in range(2,N+1):
    facto *= i

cnt = 0
while True:
    last = facto % 10
    if last != 0:
        break
    cnt += 1
    facto //= 10

print(cnt)
