# dictionary에 의상의 종류와 수를 저장한다.
# ans = (n1+1) * (n2+1) * ... - 1 (해당 종류의 옷을 입지 않는 것을 세기 위해 +1)

for _ in range(int(input())):
    clothes = dict()
    for _ in range(int(input())):
        name, kind = input().split()
        if clothes.get(kind) is None:
            clothes[kind] = 1
        else:
            clothes[kind] += 1
    ans = 1
    for values in clothes.values():
        ans *= values+1

    print(ans-1)    # 모두 입지 않는 것을 제외하기 위해 -1

