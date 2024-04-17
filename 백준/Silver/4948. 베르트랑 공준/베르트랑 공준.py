# 1부터 i 까지의 소수의 개수를 미리 저장해둔다.
# a 초과 b 이하의 소수의 개수 = f(b) - f(a)

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


memo = [-1 for _ in range(123456 * 2 + 1)]
memo[0], memo[1] = 0, 0
for i in range(2, 123456*2+1):
    if isPrime(i):
        memo[i] = memo[i-1] +1
    else:
        memo[i] = memo[i-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(memo[2*n] - memo[n])
