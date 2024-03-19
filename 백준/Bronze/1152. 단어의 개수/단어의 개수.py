# 문자열을 입력받은 후, 공백의 개수 + 1을 답으로 출력한다.
# 첫 글자와 마지막 단어가 공백인 경우 공백의 개수에 계산하지 않는다.

charList = input()
ans = 0
if len(charList) > 1:
    for i in range(len(charList)):
        if charList[i] == " ":
            if i != 0 and i != len(charList) - 1:
                ans += 1
    print(ans + 1)
else:
    if charList[0] != " ":
        print(1)
    else:
        print(0)