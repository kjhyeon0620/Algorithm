#1 2~7 8~19 20~37
#  0~5 6~17 18~35
#0  0  1 2  3 4 5
# 1 23 456 78910
#1 3 6 10 15
N = int(input())

if N == 1:
    print(1)
else:
    ans,cnt = 0,1
    val = (N-2) // 6
    while True:
        ans += cnt
        if val < ans:
            print(cnt+1)
            break
        else:
            cnt += 1