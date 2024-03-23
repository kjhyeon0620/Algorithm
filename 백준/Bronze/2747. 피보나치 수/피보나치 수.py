# top-down 방식으로 피보나치 수를 구한다.

def fibonacci(num):
    if memo[num] != -1:
        return memo[num]
    else:
        memo[num] = fibonacci(num-1) + fibonacci(num-2)
        return memo[num]
    
    
n = int(input())
memo = [0, 1] + [-1] * (n-1)
print(fibonacci(n))