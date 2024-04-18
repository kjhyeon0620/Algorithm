# set을 이용해 X에서 중복을 제거하고, 리스트에 저장한다.
# 위 리스트를 정렬한다.
# 위 리스트 값의 인덱스는 해당 값보다 적은 원소의 개수와 같다.
import sys


N = int(input())
X = list(map(int, input().split()))


newX = list(set(X))
newX.sort()
idx = dict()

for i in range(len(newX)):
    idx[newX[i]] = i

for x in X:
    sys.stdout.write(str(idx[x]) +" ")

