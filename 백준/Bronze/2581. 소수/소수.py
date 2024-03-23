# 1. 해당 숫자가 소수인지 확인하는 함수를 만든다.
# 2. M과 N을 입력받은 후, M 이상 N 이하의 숫자들을 위 함수에 대입한다.
# 3. 처음 소수가 된 수를 변수에 입력하고, 소수가 된 모든 수들을 변수에 더한다.

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


M = int(input())
N = int(input())

_min = -1
_sum = 0

for i in range(M, N+1):
    if isPrime(i):
        if not _sum:
            _min = i
        _sum += i

if _sum == 0:
    print(-1)
else:
    print(_sum)
    print(_min)