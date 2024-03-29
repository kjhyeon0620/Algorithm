# 아스키 코드를 활용하여 답을 구한다.

S = list(input())

for i in range(len(S)):
    if S[i].isalpha():
        if S[i].islower():
            S[i] = chr((ord(S[i]) - 97 + 13) % 26 + 97)
        else:
            S[i] = chr((ord(S[i]) - 65 + 13) % 26 + 65)

print("".join(S))
