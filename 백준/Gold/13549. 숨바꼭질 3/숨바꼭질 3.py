from collections import deque


N, K = map(int, input().split())
dp = [-1 for _ in range(134000)]
queue = deque()
queue.append(N)
dp[N] = 0

while queue:
    node = queue.popleft()
    if node == K:
        print(dp[K])
        break
    if node != 0:
        tmp = node
        while tmp*2 < 134000:
            if dp[tmp*2] == -1 or dp[tmp*2] > dp[node]:
                dp[tmp*2] = dp[node]
                queue.append(tmp*2)
            tmp *= 2
    if 0 <= node-1 < 134000 and dp[node-1] == -1:
        dp[node-1] = dp[node] + 1
        queue.append(node-1)
    if 0 <= node+1 < 134000 and dp[node+1] == -1:
        dp[node+1] = dp[node] + 1
        queue.append(node+1)