# 시간이 적게 걸리는 순서로 돈을 인출하면 최소 시간이 된다.

N = int(input())
Pi = list(map(int, input().split()))
Pi.sort(reverse=True)
total = 0

for i in range(N):
    total += Pi[i] * (i+1)  # i는 뒷 순서 사람의 수

print(total)
