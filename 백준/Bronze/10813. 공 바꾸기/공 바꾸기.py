# list의 index는 바구니의 번호, 원소의 값은 공의 번호로 생각해 주어진 순서대로 공을 바꾼다.
# 바구니와 공의 번호를 맞추기 위해 balls의 크기를 N+1개로 설정한다.

N, M = map(int, input().split())
balls = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    balls[i], balls[j] = balls[j], balls[i]

print(*balls[1:])