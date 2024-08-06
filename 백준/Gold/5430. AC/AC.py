# R이 나오면 rev를 반대로 바꿔 뒤집는 것 처럼 한다.
# D가 나오면 rev에 따라 첫 번쨰 혹은 마지막 숫자를 버린다.
# rev가 True이면 마지막에 출력하기 전 reverse로 뒤집어준다.

import sys
from collections import deque


input = sys.stdin.readline

for i in range(int(input())):
    func = input().rstrip()
    n = int(input())
    nums = input().rstrip()
    if nums == "[]":
        nums = []
    else:
        nums = nums[1:-1].split(",")
    nums = deque(nums)
    rev = False
    for op in func:
        if op == "R":
            rev = not rev
        else:
            if len(nums) == 0:
                nums = "error"
                break
            elif rev:
                nums.pop()
            else:
                nums.popleft()
    if nums == "error":
        print(nums)
    else:
        if rev:
            nums.reverse()
        nums = "[" + ",".join(map(str, nums)) + "]"
        print(nums)
