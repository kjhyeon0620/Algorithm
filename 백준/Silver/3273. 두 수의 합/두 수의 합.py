# 수열을 정렬한 후 투 포인터를 이용하여 두 쌍을 구한다.

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
ans = 0
left, right = 0, n-1

while left < right:
    _sum = nums[left] + nums[right]
    if _sum == x:   # 같으면 출력 후 left와 right 모두 이동
        ans, left, right = ans+1, left+1, right-1
    elif _sum > x:  # 구하는 수보다 크면 right만 이동
        right -= 1
    else:           # 구하는 수보다 작으면 left만 이동
        left += 1
print(ans)