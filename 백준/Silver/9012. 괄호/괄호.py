for _ in range(int(input())):
    stack = []
    ans = "YES"
    
    for el in input():
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
