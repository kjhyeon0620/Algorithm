# 1 부터 N까지 1로 만들기 위한 연산의 최솟값을 차례대로 저장해가며 답을 찾는다. (bottom-up)


N = int(input())

memo = [0, 0] + [-1] * (N-1) # 0, 1은 0으로 설정

for i in range(2, N+1):
    tmp = []
    if i % 3 == 0:
        tmp.append(memo[i//3] + 1)
    if i % 2 == 0:
        tmp.append(memo[i//2] + 1)
    tmp.append(memo[i-1] + 1)
    memo[i] = min(tmp)

print(memo[N])
