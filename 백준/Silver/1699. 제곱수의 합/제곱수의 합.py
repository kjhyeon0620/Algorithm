# 해당 수보다 작은 제곱수중 가장 큰 수를 계속해서 빼준다.

N = int(input())
ans = 0
memo = [x for x in range(N+1)]

for i in range(4, N+1):
    for j in range(1, int(i**0.5)+1):
        memo[i] = min(memo[i], memo[i - j**2] + 1)
print(memo[N])