N = int(input())
nums = list(map(int, input().split()))

tmp = 0

for i in range(2, N+1):     # 바로 뒤의 숫자보
    if nums[-i] < nums[-i+1]:
        tmp = i
        break

if tmp == 0:
    print(-1)
else:
    first = nums[-tmp]
    part = nums[-tmp+1:]
    for i in range(1, len(part)+1):
        if part[-i] > first:
            first, part[-i] = part[-i], first
            break
    part.sort()
    nums = nums[:-tmp] + [first] + part
    print(*nums)
