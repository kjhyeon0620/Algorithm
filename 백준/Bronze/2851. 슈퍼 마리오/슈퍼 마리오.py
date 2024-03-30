# 다음 버섯을 먹었을 때와 먹지 않았을 때 어느 경우가 100과 가까운 지를 비교 한다

scores = [int(input()) for _ in range(10)]
ans = scores[0]

for i in range(1, 10):
    if abs(100 - ans) < abs(100 - ans - scores[i]):
        break
    ans += scores[i]

print(ans)