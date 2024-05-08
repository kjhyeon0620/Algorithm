# dfs를 이용해 각 순회를 구현한다.

N = int(input())
tree = [[-1, -1] for _ in range(N+1)]
for i in range(N):
    root, left, right = input().split()
    root = ord(root) - 64
    if left != ".":
        tree[root][0] = ord(left)-64
    if right != ".":
        tree[root][1] = ord(right)-64

# 전위 순회

stack = [1]
visited = [False for _ in range(N+1)]
ans = []

while stack:
    node = stack.pop()
    if visited[node]:
        continue
    visited[node] = True
    ans.append(node)                # 방문한 노드는 부모이므로 ans 에 넣는다.
    if tree[node][1] != -1:         # stack 이므로 오른쪽 자식 노드부터 넣는다
        stack.append(tree[node][1])
    if tree[node][0] != -1:
        stack.append(tree[node][0])

print("".join(map(lambda a: chr(a+64), ans)))

# 중위 순회
stack = [1]
visited = [False for _ in range(N+1)]
ans = []

while stack:
    node = stack.pop()
    if visited[node]:
        continue
    if tree[node][0] == -1 or visited[tree[node][0]]:   # 왼쪽 자식이 없거나 이미 방문했을 경우 루트를 ans 에 넣는다.
        ans.append(node)
        visited[node] = True
        if tree[node][1] != -1:                         # 오른쪽 자식이 존재할 경우 stack 에 넣는다.
            stack.append(tree[node][1])                 # 부모보다 오른쪽 자식이 먼저 방문하지 않으므로 visited 는 검사하지 않는다.
        continue
    if tree[node][1] != -1:                             # 왼쪽 자식에 방문하지 않았을 경우 오른쪽 자식부터 stack 에 넣는다.
        stack.append(tree[node][1])
    stack.append(node)
    stack.append(tree[node][0])

print("".join(map(lambda a: chr(a+64), ans)))

# 후위 순회

stack = [1]
visited = [False for _ in range(N+1)]
ans = []

while stack:
    node = stack.pop()
    if visited[node]:
        continue        # 왼쪽 자식과 오른쪽 자식 모두 없거나 방문했을 경우에 부모를 ans 에 넣는다.
    if (tree[node][0] == -1 or visited[tree[node][0]]) and (tree[node][1] == -1 or visited[tree[node][1]]):
        ans.append(node)
        visited[node] = True
        continue
    stack.append(node)  # 그렇지 않을 경우 부모부터 차례대로 stack에 넣는다.
    if tree[node][1] != -1 and not visited[tree[node][1]]:
        stack.append(tree[node][1])
    if tree[node][0] != -1 and not visited[tree[node][0]]:
        stack.append(tree[node][0])

print("".join(map(lambda a: chr(a+64), ans)))
