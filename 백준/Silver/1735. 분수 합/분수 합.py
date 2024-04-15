# 분수의 합을 구한 후 최대공약수를 이용해 약분한다.


def maxDivisor(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2:
        num1, num2 = num2, num1 % num2,
    return num1


A1, B1 = map(int, input().split())
A2, B2, = map(int, input().split())
ansA, ansB = A2 * B1 + A1 * B2, B1 * B2
divs = maxDivisor(ansA, ansB)

print(ansA // divs, ansB // divs)

