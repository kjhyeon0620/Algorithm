from collections import deque


N = int(input())

cards = deque([i for i in range(1, N+1)])

for _ in range(N-1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())
