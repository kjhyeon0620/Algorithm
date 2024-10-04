N, K = map(int, input().split())

nums = list(range(1, N+1))
tmp = K-1
length = N
ans = []
for _ in range(N):
    tmp %= length
    ans.append(nums.pop(tmp))
    tmp += K-1
    length -= 1
print("<" + ", ".join(map(str, ans)) + ">")