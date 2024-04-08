# stack을 이용하여 짝을 맞춘다.

import sys


input = sys.stdin.readline

while True:
    stack = []
    inp = input().rstrip()
    if inp == ".":
        break
    flag = True
    for ch in inp:
        if ch == "[" or ch == "(":
            stack.append(ch)

        elif ch == "]":
            if len(stack) == 0 or stack.pop() != "[":
                flag = False
                break

        elif ch == ")":
            if len(stack) == 0 or stack.pop() != "(":
                flag = False
                break
    if stack:
        flag = False

    if flag:
        print("yes")
    else:
        print("no")
