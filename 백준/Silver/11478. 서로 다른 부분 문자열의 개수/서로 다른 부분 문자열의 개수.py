# slicing을 이용해 부분 문자열을 구한 후 집합에 집어넣어 중복을 없앤다.

ans = set()
S = input()
length = len(S)
for i in range(length):
    for j in range(i+1, length+1):
        ans.add(S[i:j])
print(len(ans))