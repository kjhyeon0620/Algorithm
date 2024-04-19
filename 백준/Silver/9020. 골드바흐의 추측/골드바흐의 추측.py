# 2부터 9998까지 소수라면 1, 아니라면 0을 반환하도록 한다.
# 검사하기 전에는 -1을 저장해둔다.

def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1


T = int(input())
memo = [-1] * 9999

for _ in range(T):
    n = int(input())
    for i in range(n // 2, 1, -1):
        if memo[i] == -1:
            memo[i] = isPrime(i)
        if memo[i] == 0:
            continue
        if memo[n-i] == -1:
            memo[n-i] = isPrime(n-i)
        if memo[n-i] == 1:
            print(i, n-i)
            break
