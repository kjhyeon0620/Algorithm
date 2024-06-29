# (n+9) C n

def factorial(num):
    if num == 1:
        return 1
    if memo[num] != -1:
        return memo[num]
    else:
        memo[num] = factorial(num-1) * num
        return memo[num]


N = int(input())
memo = [-1] * (N+10)

print((factorial(N+9) // factorial(N) // factorial(9)) % 10007)