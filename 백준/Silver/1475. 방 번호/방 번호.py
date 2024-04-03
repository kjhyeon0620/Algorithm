# 0 ~ 9 까지 개수를 모두 센 후 가장 큰 수를 출력한다.
# 단, 6과 9는 함께 세며 2로 나눈 후 계산한다.

N = list(map(int, input()))
nums = [0] * 9

for num in N:
    if num == 9:
        nums[6] += 1
    else:
        nums[num] += 1
if nums[6] % 2 == 0:
    nums[6] //= 2
else:
    nums[6] = nums[6] // 2 + 1
    
print(max(nums))