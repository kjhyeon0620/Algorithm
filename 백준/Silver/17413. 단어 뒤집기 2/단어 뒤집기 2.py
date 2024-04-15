# 단어이면 스택, 태그이면 큐를 사용해 단어를 출력한다
# inTag를 boolean을 이용하여 태그 안과 밖을 구분한다.

from collections import deque


S = input()
ans = ""
tmp = deque()
inTag = False

for ch in S:
    if ch == ">":
        while tmp:
            ans += tmp.popleft()
        ans += ">"
        inTag = False
    elif ch == "<":
        while tmp:
            ans += tmp.pop()
        tmp.append("<")
        inTag = True
    elif ch == " " and not inTag:
        while tmp:
            ans += tmp.pop()
        ans += " "
    else:
        tmp.append(ch)

while tmp:
    ans += tmp.pop()    # 마지막에 단어가 있을 경우 위 for 문에서 pop되지 않으므로 직접 해줌
    
print(ans)