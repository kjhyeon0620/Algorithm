# dfs를 이용해 오름차순을 만족하며 길이가 L인 문자열을 모두 구한다.
# 모음과 자음 조건을 만족한다면 출력한다.

L, C = map(int, input().split())
characters = list(input().split())
characters.sort()
stack = ""


def check(tmp):
    m = ["a", "e", "i", "o", "u"]
    lenJ = 0
    lenM = 0
    for ch in tmp:
        if ch in m:
            lenM += 1
        else:
            lenJ += 1

    if lenJ >= 2 and lenM >= 1:
        return True
    else:
        return False


def dfs(start):
    global stack

    if len(stack) == L:
        if check(stack):
            print(stack)
        return

    for i in range(start, C):
        stack = stack + characters[i]
        dfs(i+1)
        stack = stack[:-1]


dfs(0)
