N = int(input())
hasCards = list(map(int, input().split()))
M = int(input())
findCards = list(map(int, input().split()))
cards = dict()

for hc in hasCards:
    cards[hc] = 1

for fc in findCards:
    if cards.get(fc) is None:
        print("0", end=" ")
    else:
        print("1", end=" ")

