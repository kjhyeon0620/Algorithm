# dfs를 이용하여 부등호 순서를 만족하는 모든 경우의 수를 구한다.

k = int(input())
operators = list(input().split())

visited = [False] * 10
maxAns = ""
minAns = ""


def check(n1, n2, o):
    if o == ">":
        return n1 > n2
    else:
        return n1 < n2


def dfs(depth, s):
    global minAns, maxAns

    if depth == k+1:
        if len(minAns) == 0:
            minAns = s
        else:
            maxAns = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(int(s[-1]), i, operators[depth-1]):  # 길이가 0이거나, 부등호 관계를 만족하면
                visited[i] = True
                dfs(depth+1, s+str(i))
                visited[i] = False


dfs(0, "")
print(maxAns)
print(minAns)
