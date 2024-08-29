N = int(input())
for i in range(N//5, -1, -1):
    if (N - (i * 5)) % 3 == 0:
        print(i + (N - (i * 5)) // 3)
        exit(0)
print(-1)
