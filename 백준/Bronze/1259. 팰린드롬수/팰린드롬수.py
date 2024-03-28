# 길이가 1일때 / 2,3일때 / 4,5일때를 나누어 확인한다.

while True:
    num = input()
    if num == "0":
        break
    length = len(num)

    if length == 1:
        print("yes")
    elif length <= 3:
        if num[0] == num[-1]:
            print("yes")
        else:
            print("no")
    else:
        if num[0] == num[-1] and num[1] == num[-2]:
            print("yes")
        else:
            print("no")
