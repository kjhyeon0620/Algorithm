# 한 자리씩 16의 제곱수를 곱해가며 계산한다.
# A ~ F는 아스키코드를 통해 값을 구한다. (아스키코드 값 - 55)

inp = input()
cnt = 1
ans = 0
length = len(inp)

while inp != "":
    num = inp[length-1]
    if num.isalpha():
        num = ord(num) - 55
    else:
        num = int(num)
    ans += num * cnt
    cnt *= 16
    inp = inp[:length-1]
    length -= 1


print(ans)