n = int(input())
nums = list(map(int, input().split()))
setList = list(set(nums))
setList.sort()
idx = dict()

for i in range(len(setList)):
    idx[setList[i]] = i

for num in nums:
    print(idx[num], end=" ")
