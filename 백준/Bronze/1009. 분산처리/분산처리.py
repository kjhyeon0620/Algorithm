# a의 일의 자리가 무엇인지에 따라 경우를 나누어 계산한다.
# 1 -> 1
# 2 -> 2 4 8 6 2 4 8 6 ... 반복
# 3 -> 3 9 7 1 3 9 7 1 ... 반복
# 4 -> 4 6 4 6 ... 반복
# 5 -> 5
# 6 -> 6
# 7 -> 7 9 3 1 7 9 3 1 ... 반복
# 8 -> 8 4 2 6 8 4 2 6 ... 반복
# 9 -> 9 1 9 1 ... 반복
# 0 -> 0(10번)

T = int(input())
list1 = [1, 5, 6]
list2 = [4, 9]
list4 = [2, 3, 6, 8]

for _ in range(T):
    a, b = map(int, input().split())
    base = a % 10

    if base == 0:
        print(10)
    elif base in list1:
        print(base)
    elif base in list2:
        print((base ** (((b+1) % 2) + 1)) % 10)
    else:
        print((base ** (((b-1) % 4) + 1)) % 10)