# 소수인지 검사하는 소수를 만든다.
# M부터 N까지 수를 위 함수에 넣는다.

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
