# pN -> 0, 2, 4, ... 2N 인덱스가 I이고 1, 3, ... 2N-1 인덱스가 O인 문자열
# 모든 구간을 돌며 pN이 포함되어 있는 구간의 개수를 센다.

N = int(input())
M = int(input())
S = input()

cnt = 0

for i in range(M-(2*N)):
    flag = True
    for j in range(2*N + 1):
        if (j % 2 == 0 and S[i+j] != "I") or (j % 2 == 1 and S[i+j] != "O"):
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)