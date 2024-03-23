change = 1000 - int(input())
cnt = 0
coins = [500, 100, 50, 10, 5, 1]

for i in range(6):
    if change == 0:
        break
    cnt += change // coins[i]
    change = change % coins[i]

print(cnt)