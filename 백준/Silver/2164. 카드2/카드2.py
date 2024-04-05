# deque의 popleft를 이용해서 문제를 해결한다.

from collections import deque

N = int(input())
cards = deque(range(1, N+1))

for _ in range(N-1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])

