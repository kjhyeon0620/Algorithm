# stack을 이용한다.
# (가 입력되면 append, )가 입력되면 pop을 실행하여 VPS인지 판단한다.


T = int(input())

for _ in range(T):
    inp = input()
    stack = []
    ans = "YES"
    
    for el in inp:
        if el == "(":
            stack.append(el)
        else:
            if len(stack) == 0:
                ans = "NO"
                break
            stack.pop()
            
    if stack:
        print("NO")
    else:
        print(ans)
