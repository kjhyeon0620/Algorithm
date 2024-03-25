# 최대 공약수를 먼저 구한 후, 이를 이용해 최소 공배수를 구한다.

a, b = map(int, input().split())
maxCommonFactor = 1
for i in range(min(a, b), 1, -1):
    if a % i == 0 and b % i == 0:
        maxCommonFactor = i
        break

print(maxCommonFactor)
print(maxCommonFactor * (a // maxCommonFactor) * (b // maxCommonFactor))