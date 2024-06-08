# DP를 이용한다.
# 해당 위치까지의 최댓값을 저장한다.
# 단, 해당 위치의 스티커는 꼭 사용하는 것으로 한다.

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = []

    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    if n == 1:  # n이 1이면 두 개의 스티커 중 큰 값을 출력한다.
        print(max(stickers[0][0], stickers[1][0]))
        continue

    stickers[0][1] = stickers[1][0] + stickers[0][1]    # 1번째 줄 2번째 스티커 까지의 최댓값은 2번째 줄 1번째 스티커와 해당 스티커를 더한 값이다.
    stickers[1][1] = stickers[0][0] + stickers[1][1]    # 2번째 줄 2번째 스티커 까지의 최댓값은 1번째 줄 1번째 스티커와 해당 스티커를 더한 값이다.

    for i in range(2, n):
        for j in range(2):
            stickers[j][i] = max(stickers[(j+1) % 2][i-1], stickers[(j+1) % 2][i-2]) + stickers[j][i]
        # 다른 줄의 2번째 전 스티커까지의 최댓값과 다른 줄의 1번째 전 스티커까지의 최댓값 중 더 큰 값을 해당 위치의 스티커와 더하면 최댓값이 된다.
    print(max(stickers[0][-1], stickers[1][-1]))
