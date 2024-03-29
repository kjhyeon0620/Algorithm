# 1부터 수열을 계속해서 이어나간다.
# cnt 변수를 이용하여 수열이 B 번째 숫자를 나타내면 합을 구한다.

A, B = map(int, input().split())
arr = []
cnt = 0
tmp = 1

while cnt < B:
    for i in range(tmp):
        arr.append(tmp)
        cnt += 1
    tmp += 1

print(sum(arr[A-1:B]))
