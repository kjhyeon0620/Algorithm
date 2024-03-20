# 1. 문자열을 입력받고, 한 문자씩 확인하여 그에 맞는 동작을 한다.
# 2. O일 경우, tmp 변수를 증가시키고, ans 변수에 더한다.
# 3. X일 경우, tmp 변수를 0으로 초기화시킨다.

T = int(input())

for _ in range(T):
    inp = input()
    tmp, ans = 0, 0

    for ch in inp:
        if ch == "O":
            tmp += 1
            ans += tmp
        else:
            tmp = 0
    print(ans)