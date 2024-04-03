# 1,2,3 ... 로 주어진 수열의 합이 S를 넘을 때 해당 수열의 갯수 에서 1을 빼면 N의 최댓값이 나온다.

S = int(input())
ans = 1
tmp = 0

while True:
    tmp += ans
    if tmp > S:
        print(ans-1)
        break
    ans += 1

