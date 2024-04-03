# % 를 이용해 해당하는 숫자를 1부터 증가시키며 찾는다.

E, S, M = map(int, input().split())

ans = 1
while True:
    if (ans-1) % 15 + 1 == E and (ans-1) % 28 + 1 == S and (ans-1) % 19 + 1 == M:
        break
    ans += 1

print(ans)