N = int(input())

status = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        status[i][j] += status[j][i]

start = [0]
ans = []
visited = [False for _ in range(N)]


def dfs(first):
    if len(start) == N//2:
        link = []
        for i in range(N):
            if i not in start:
                link.append(i)
        score_start = 0
        score_link = 0

        for i in range(N//2):
            for j in range(i+1, N//2):
                score_start += status[start[i]][start[j]]
                score_link += status[link[i]][link[j]]
        ans.append(abs(score_start-score_link))
        return

    for i in range(first+1, N):
        if not visited[i]:
            start.append(i)
            visited[i] = True
            dfs(i)
            start.pop()
            visited[i] = False


dfs(0)
print(min(ans))
