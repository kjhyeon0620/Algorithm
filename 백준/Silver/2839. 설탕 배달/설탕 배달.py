N = int(input())

cnt5 = N // 5
ans = -1

while cnt5 >= 0:
    if (N - (cnt5 * 5)) % 3 == 0:
        ans = cnt5 + (N - (cnt5 * 5)) // 3
        break
    cnt5 -= 1

print(ans)