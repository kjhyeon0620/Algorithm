# list 에 점수를 담고, 정렬한 후 해당하는 등수의 점수를 인덱스를 통해 접근한다.

N, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)

print(scores[k-1])