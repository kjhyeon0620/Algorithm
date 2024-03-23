# 각 자릿수 별로 계산한다.
# isalpha() 함수를 통해 알파벳이면 아스키코드를 통해 값을 계산한다.

N, B = input().split()
B = int(B)
cnt = 1
ans = 0
length = len(N)

while N != "":
    num = N[length-1]
    N = N[:length-1]
    length -= 1

    if num.isalpha():
        num = ord(num) - 55
    else:
        num = int(num)
    ans += num * cnt
    cnt *= B

print(ans)