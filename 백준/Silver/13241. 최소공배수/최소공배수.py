# 최대공약수를 구하고 이를 이용하여 최소공배수를 구한다.

A, B = map(int, input().split())

_min, _max = min(A, B), max(A, B)
cnt = 0
divs = []

for i in range(1, int(_min ** 0.5) + 1):
    if _min % i == 0:
        cnt += 1
        divs.append(i)

for i in range(cnt-1, -1, -1):
    divs.append(_min // divs[i])

for i in range(2*cnt-1, -1, -1):
    if _max % divs[i] == 0:
        print(divs[i] * (_max // divs[i]) * (_min // divs[i]))
        break
