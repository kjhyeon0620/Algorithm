# 레이저가 지날 때 현재 지나고 있는 쇠막대기의 개수만큼 추가하면 된다.

inp = input()
cnt = 0
tmp = 0

for i in range(len(inp)):
    if inp[i] == "(":
        tmp += 1        # 지나는 막대기 개수 1개 추가

    elif inp[i] == ")":
        if inp[i-1] == "(": # 레이저가 지나갈 때
            tmp -= 1        # 이전에 (를 막대기로 계산했기에 1 뺀다
            cnt += tmp      # 지나가는 막대기 개수만큼 cnt tmp 만큼 증가
        else:               # 막대기의 끝점일 때
            cnt += 1        # cnt 1 증가
            tmp -= 1        # tmp 1 감소

print(cnt)