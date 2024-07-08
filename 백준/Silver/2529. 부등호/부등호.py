# dfs를 이용하여 부등호 순서를 만족하는 모든 경우의 수를 구한다.

k = int(input())
operators = list(input().split())
ans = []
visited = [False] * 10


def dfs(num):
    if len(tmp) == k+1:
        ans.append("".join(map(str, tmp)))
        return
    op = operators[len(tmp)-1]
    for i in range(0, 10):
        if not visited[i]:
            if (op == "<" and num < i) or (op == ">" and num > i):
                visited[i] = True
                tmp.append(i)
                dfs(i)
                visited[i] = False
                tmp.pop()


for j in range(10):
    tmp = [j]
    visited[j] = True
    dfs(j)
    tmp.pop()
    visited[j] = False

print(ans[-1])
print(ans[0])