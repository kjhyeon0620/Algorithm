# 1. [-1] * 26 리스트를 만든다
# 2. 문자열을 입력받고, 문자열을 돌며 리스트의 (해당 문자의 아스키코드 - 97) 인덱스에 해당 문자의 위치를 입력한다.
# 3. 다만, 해당 위치의 값이 -1이 아닐 경우 넘어간다.

ans = [-1] * 26
inp = input()

for i in range(len(inp)):
    num = ord(inp[i]) - 97
    if ans[num] == -1:
        ans[num] = i

print(*ans)
