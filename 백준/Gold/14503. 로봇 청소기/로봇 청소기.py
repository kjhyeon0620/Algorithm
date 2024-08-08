N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]  # 북 동 남 서 순서로 설정했다. 반시계 방향으로 회전할 때 1씩 인덱스를 줄이면 된다.
dx = [0, 1, 0, -1]
ans = 0

while True:
    if room[r][c] == 0: # 현재 칸이 청소되지 않았으면 ans를 1 증가시키고 청소한 칸으로 바꾼다.
        ans += 1
        room[r][c] = 2
    flag = False        # 주변 4칸 중 청소되지 않은 칸이 있다면 flag를 True로 바꾼다.
    for i in range(4):
        nd = (d-i-1) % 4    # 반시계 방향으로 90도 먼저 회전한 후 순서대로 청소 여부를 확인한다. 
        nr = r + dy[nd]     # 청소되지 않은 칸이 있다면 그 칸으로 이동한다.
        nc = c + dx[nd]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r = nr
            c = nc
            d = nd
            flag = True
            break
    if not flag:            # 주변 4칸 중 청소되지 않은 칸이 없을 때 실행한다.
        backR = r + dy[(d-2) % 4]   # 바라보는 방향 기준 뒤의 칸이 벽인 경우 프로그램을 중단하고, 아니라면 해당 칸으로 이동한다.
        backC = c + dx[(d-2) % 4]
        if 0 <= backR < N and 0 <= backC < M and room[backR][backC] != 1:
            r = backR
            c = backC
        else:
            break
print(ans)


