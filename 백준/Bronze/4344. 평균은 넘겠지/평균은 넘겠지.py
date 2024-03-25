# 각 케이스에 대해 평균을 구한 후 평균을 넘는 학생의 비율을 계산한다.

C = int(input())

for _ in range(C):
    inp = list(map(int, input().split()))
    N = inp[0]
    scores = inp[1:]
    average = sum(scores) / N
    ans = len(list(filter(lambda x : x > average, scores)))
    print(round(ans / N * 100, 3), end="")
    print("%")