# S에서 IOI 의 개수를 센다.

N = int(input())
M = int(input())
S = input()
nums = []
tmp = -1
ans = 0

for i in range(M-1):
    if S[i] == "I":
        if tmp == -1:
            tmp = 0
        else:
            if S[i+1] == "I":
                nums.append(tmp)
                tmp = -1
    else:
        if tmp != -1:
            if S[i+1] == "I":
                tmp += 1
            else:
                nums.append(tmp)
                tmp = -1

if tmp != -1:
    nums.append(tmp)
for num in nums:
    if num >= N:
        ans += num - N + 1

print(ans)

