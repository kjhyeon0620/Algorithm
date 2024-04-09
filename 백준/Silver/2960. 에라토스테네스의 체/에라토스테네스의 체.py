# 주어진 순서대로 수를 지운다.

N, K = map(int, input().split())
cnt = 0
arr = list(range(2, N+1))

while True:
    _min = arr[0]
    cnt += 1
    if cnt == K:
        print(_min)
        break
    for i in range(1, len(arr)):
        if arr[i] % _min == 0:
            cnt += 1
            if cnt == K:
                print(arr[i])
                exit(0)

    arr = list(filter(lambda x: x % _min != 0, arr))

