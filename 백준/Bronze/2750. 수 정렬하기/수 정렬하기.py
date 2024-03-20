# 각 숫자들을 입력받아 list에 넣은 후, list의 sort() 함수를 활용하여 정렬한다.

N = int(input())
arr = []

for _ in range(N):
    inp = int(input())
    arr.append(inp)

arr.sort()

for num in arr:
    print(num)