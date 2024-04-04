# 0으로 이루어진 연속된 수의 갯수와 1로 이루어진 연속된 수의 갯수 중 작은 값이 정답이다.

S = input()
cnt = dict({"0": 0, "1": 0})
prev = S[0]

for ch in S:
    if ch != prev:
        cnt[prev] += 1
        prev = ch
        
cnt[S[-1]] += 1 # 이전과 다른 경우에만 카운트되므로 마지막 덩어리는 처리되지 않기에 따로 처리한다. 
# 
print(cnt["0"] if cnt["0"] <= cnt["1"] else cnt["1"])