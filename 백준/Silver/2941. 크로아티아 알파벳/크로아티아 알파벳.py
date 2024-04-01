# 단어 전체의 길이를 구한 다음, 아래 경우에 해당하는 만큼을 뺀 후 정답으로 출력한다
# 1. "-"가 나온 경우 2글자를 1글자로 세기에 1을 뺀다
# 2. "="이 나온 경우
# 2-1. 앞 글자가 "z"가 아닌 경우 1을 뺀다
# 2-2. 앞 글자가 "dz"인 경우 2를 뺀다
# 2-3. 앞 글자가 "z"인 경우 1을 뺀다
# 3. "lj", "nj"의 경우 1을 뺀다

word = input()
length = len(word)
ans = length

for i in range(1, length):
    if word[i] == "-":  # c-, d-인 경우
        ans -= 1
    elif word[i] == "=":
        if word[i-1] != "z":    # c= , s= 인 경우
            ans -= 1
        else:
            if i == 1:  # z=인 경우 (i가 1일때 i-2를 할 수 없기에 미리 제외)
                ans -= 1
            elif word[i-1] == "z" and word[i-2] == "d": # dz=인 경우
                ans -= 2
            else:   # z=인 경우
                ans -= 1
    elif word[i] == "j" and (word[i-1] == "l" or word[i-1] == "n"): # lj, nj인 경우
        ans -= 1

print(ans)


