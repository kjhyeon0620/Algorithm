# 주어진 연산을 수행하는 함수를 만든다.
# 리턴값이 자기 자신이 나올 때까지 함수를 실행한다.
# cnt 변수를 이용하여 횟수를 계산한다.

def solution(num):
    if num < 10:
        return num*11
    else:
        return 10 * (num % 10) + (num // 10 + num % 10) % 10


N = int(input())
cnt = 1
res = solution(N)

while True:
    if N == res:
        break
    res = solution(res)
    cnt += 1

print(cnt)