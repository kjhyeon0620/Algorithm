# 2부터 주어진 수의 제곱근까지 나눠진다면 계속해서 나눈다.
# 합성수의 경우는 이미 해당 수의 약수인 소수에 의해 나눠졌기 때문에 고려할 필요가 없다.

N = int(input())

if N != 1:
    for i in range(2, int(N ** 0.5) + 1):
        while N % i == 0:
            print(i)
            N //= i
    if N != 1:
        print(N)