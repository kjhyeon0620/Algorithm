# 총감독관 1명을 계산한 후, 나머지를 부감독관으로 계산한다.

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for el in A:
    cnt += 1
    el -= B
    if el <= 0:
        continue
    if el % C == 0:
        cnt += el // C
    else:
        cnt += el // C + 1

print(cnt)