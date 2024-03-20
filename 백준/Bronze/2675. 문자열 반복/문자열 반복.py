# 숫자와 문자열을 입력받은 후, 빈 문자열에 주어진 숫자만큼 반복하여 추가한다.

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    ans = ""
    for ch in S:
        ans += ch * R
    print(ans)