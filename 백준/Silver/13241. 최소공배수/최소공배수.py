A, B = map(int, input().split())
ans = A * B
while A:
    if A < B:
        A, B = B, A
    A %= B
print(ans // B)