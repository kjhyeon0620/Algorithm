# 첫 번째 문장을 기준으로 다른 부분을 모두 ?로 출력한다.

N = int(input())
arr = [input() for _ in range(N)]
different = []
length = len(arr[0])

for i in range(1, N):
    for j in range(length):
        if j not in different and arr[0][j] != arr[i][j]:
            different.append(j)

for i in range(length):
    if i in different:
        print("?", end="")
    else:
        print(arr[0][i], end="")