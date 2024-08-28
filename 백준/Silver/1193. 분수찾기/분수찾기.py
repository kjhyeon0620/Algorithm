X = int(input())
tmp = 1
while True:
    val = (tmp * (tmp + 1)) // 2
    if val >= X:
        break
    tmp += 1
num1 = X - val + tmp
num2 = tmp - num1 + 1
if tmp % 2 == 0:
    print(f'{num1}/{num2}')
else:
    print(f'{num2}/{num1}')
