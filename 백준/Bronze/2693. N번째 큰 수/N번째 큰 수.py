# 배열을 정렬한 후 3번째로 큰 수를 출력한다

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])