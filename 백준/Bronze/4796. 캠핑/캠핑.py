cnt = 0

while True:
    L, P, V = map(int, input().split())
    cnt += 1
    if not (L or P or V):
        break

    print("Case " + str(cnt) + ": ", end="")
    if V % P >= L:
        print(L * (V // P) + L)
    else:
        print(L * (V // P) + V % P)