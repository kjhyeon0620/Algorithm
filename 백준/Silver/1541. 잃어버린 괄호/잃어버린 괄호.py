# -가 나오면 뒤에 있는 모든 수를 음수로 만들 수 있다.
#(+가 나오면 괄호로 묶을 수 있음)

nums = []
ops = []
num = ""
flag = False
for ch in input():
    if ch == "+" or ch == "-":
        nums.append(int(num))
        num = ""
        ops.append(ch)
    else:
        num += ch
nums.append(int(num))
ans = nums[0]

for i in range(len(ops)):
    if flag or ops[i] == "-":
        flag = True
        ans -= nums[i+1]
    else:
        ans += nums[i+1]

print(ans)