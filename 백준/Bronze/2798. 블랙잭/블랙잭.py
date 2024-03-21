# 1. N, M, 카드를 입력받는다.
# 2. cards 를 정렬한 후, 삼중 for 문으로 모든 3개에 조합을 계산한다.
# 3. 다만, 합이 이미 M을 넘어가면 마지막 for 문은 무의미하므로 break

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
blackjack = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            _sum = cards[i] + cards[j] + cards[k]
            if _sum > M:
                break
            elif _sum > blackjack:
                blackjack = _sum

print(blackjack)
