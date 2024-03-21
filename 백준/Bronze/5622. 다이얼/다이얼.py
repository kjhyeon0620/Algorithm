# 1. 리스트를 활용하여 문자를 초로 변환할 수 있게 한다.
# 2. 문자의 각 알파벳들을 초로 변환하여 ans에 더한다.

arr = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
ans = 0

word = input()

for ch in word:
    for i in range(8):
        if ch in arr[i]:
            ans += i+3
            break
print(ans)
