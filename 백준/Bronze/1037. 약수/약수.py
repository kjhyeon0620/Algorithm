# 진짜 약수를 리스트에 저장한 후 정렬한다
# 가장 작은 값과 큰 값을 곱하면 N이 나온다.

T = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[0] * arr[T-1])