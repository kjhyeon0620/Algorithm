S = input()
prev = "2"
cnt = [0, 0]
for num in S:
    if num != prev:
        cnt[int(num)] += 1
        prev = num

print(cnt[0] if cnt[0] < cnt[1] else cnt[1])