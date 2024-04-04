# 리스트에 저장하여 정렬한 후 해당하는 인덱스의 값을 출력한다.

N, K = map(int, input().split())
nums = list(map(int, input().split()))

print(sorted(nums)[K-1])
