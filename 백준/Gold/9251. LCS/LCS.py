# 첫 번째 문자의 i 번째 까지, 두 번째 문자의 j 번째 까지 봤을 때 최장 공통 부분 수열을 dp에 저장한다.

s1 = input()
s2 = input()
len1 = len(s1)
len2 = len(s2)
dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
