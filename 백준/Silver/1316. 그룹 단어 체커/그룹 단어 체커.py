# 26 크기의 리스트를 만들어 알파벳이 나온 적이 있는지 확인할 수 있도록 한다.

N = int(input())
cnt = 0

for _ in range(N):
    isFirst = [True] * 26   # 등장한 적이 있으면 False
    word = input()
    flag = True             # 그룹 단어가 아닌 경우 False
    isFirst[ord(word[0])-97] = False    # i-1을 사용하기 위해 0번째 인덱스만 미리 설정

    for i in range(1, len(word)):
        if word[i] != word[i-1]:    # 연속되지 않은 경우에
            if isFirst[ord(word[i])-97]:    # 이 단어에서 처음 등장한 경우에는
                isFirst[ord(word[i])-97] = False    # isFirst를 False로
            else:                           # 등장한 적이 있는 경우에는
                flag = False                        # flag를 False로 하고 break로 하여 그룹 단어로 세지 않는다.
                break

    if flag:
        cnt += 1

print(cnt)
