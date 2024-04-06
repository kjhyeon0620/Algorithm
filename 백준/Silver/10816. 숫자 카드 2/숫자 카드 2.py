# dictionary를 이용하여 해당 숫자의 개수를 출력한다.

N = int(input())
cards = list(map(int, input().split()))
cnt = dict()

for card in cards:
    if cnt.get(card) is None:
        cnt[card] = 1
    else:
        cnt[card] += 1

M = int(input())

for num in map(int, input().split()):
    if cnt.get(num) is None:
        print(0, end=" ")
    else:
        print(cnt[num], end=" ")