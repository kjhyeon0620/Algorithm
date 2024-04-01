# N개의 리스트를 만들어 덩치가 큰 사람의 수를 저장한다.
# for문을 활용해 N명 중 2명을 뽑아 두 사람의 덩치를 비교한다.

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
ans = [1] * N # 등수 = 덩치가 큰 사람 수 + 1 이므로 1로 초기화한다

for i in range(N-1):
    for j in range(i+1, N):
        if info[i][0] > info[j][0] and info[i][1] > info[j][1]:
            ans[j] += 1
        elif info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            ans[i] += 1

print(*ans)
