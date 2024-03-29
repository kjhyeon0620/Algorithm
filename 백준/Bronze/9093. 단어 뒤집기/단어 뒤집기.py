# split()으로 단어를 나누어 리스트에 저장한 후, 각 문자열을 뒤집어 출력한다.

T = int(input())

for _ in range(T):
    words = list(input().split())

    for i in range(len(words)):
        words[i] = words[i][::-1]

    print(" ".join(words))

