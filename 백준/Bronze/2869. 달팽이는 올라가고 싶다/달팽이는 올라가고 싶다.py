# 매일 (A-B)m 만큼 올라가지만, 마지막 날에는 A 만큼 올라가므로
# (V-A) m 까지 (A-B) m/일 로 계산한 후 1일을 더하면 답이다.

A, B, V = map(int, input().split())
day = (V - A) // (A - B)

if (V - A) % (A - B) == 0:
    print(day + 1)
else:
    print(day + 2)