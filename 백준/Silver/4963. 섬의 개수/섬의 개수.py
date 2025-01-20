while True:
    w, h = map(int, input().split())
    
    if w == 0:
        break
        
    board = []
    
    for _ in range(h):
        board.append(list(map(int, input().split())))

    ans = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    d = [-1, 0, 1]
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                ans += 1
                stack = [[i, j]]
                visited[i][j] = True

                while stack:
                    node = stack.pop()
                    y, x = node[0], node[1]
                    for dy in d:
                        for dx in d:
                            ny = y+dy
                            nx = x+dx
                            if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == 1 and not visited[ny][nx]:
                                stack.append([ny, nx])
                                visited[ny][nx] = True
    print(ans)
