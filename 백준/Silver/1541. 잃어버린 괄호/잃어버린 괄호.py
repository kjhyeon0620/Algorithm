exp = input()
tmp = ""
ans = 0
isMinusExist = False
for ch in exp:
    if ch.isalnum():
        tmp += ch
    elif isMinusExist:
        ans -= int(tmp)
        tmp = ""
    else:
        if ch == "-":
            isMinusExist = True
        ans += int(tmp)
        tmp = ""

if isMinusExist:
    print(ans - int(tmp))
else:
    print(ans + int(tmp))


