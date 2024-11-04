N = int(input())
vals = list(map(int, input().split()))

vals.sort(reverse=True)
left, right = 0, N-1
diff = abs(vals[left]+vals[right])
ans = [vals[left], vals[right]]

while left < right:
    if diff > abs(vals[left]+vals[right]):
        ans[0], ans[1] = vals[left], vals[right]
        diff = abs(vals[left] + vals[right])
    if abs(vals[left] > abs(vals[right])):
        left += 1
    else:
        right -= 1

ans.sort()
print(*ans)

