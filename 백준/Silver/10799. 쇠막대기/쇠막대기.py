inp = input()
ans = 0
tmp = 0

for i in range(len(inp)):
    if inp[i] == "(":
        if inp[i+1] == "(":
            ans += 1
            tmp += 1
    else:
        if inp[i-1] == "(":
            ans += tmp
        else:
            tmp -= 1

print(ans)