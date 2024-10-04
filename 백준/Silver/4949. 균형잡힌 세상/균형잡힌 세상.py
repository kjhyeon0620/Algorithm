import sys


input = sys.stdin.readline

while True:
    st = input().rstrip()
    if st == ".":
        break
    stack = []
    ans = "yes"
    for ch in st:
        if ch == "(" or ch == "[":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack.pop() != "(":
                ans = "no"
                break
        elif ch == "]":
            if not stack or stack.pop() != "[":
                ans = "no"
                break
    if stack:
        ans = "no"
    print(ans)