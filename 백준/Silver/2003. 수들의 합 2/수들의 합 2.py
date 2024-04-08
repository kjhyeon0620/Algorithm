# 2중 for 문을 이용해 답을 구한다.

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

for i in range(N):
    tmp = A[i]
    
    if tmp == M:
        cnt += 1
        continue
    elif tmp > M:
        continue
        
    for j in range(i+1, N):
        tmp += A[j]
        
        if tmp == M:
            cnt += 1
            break
        elif tmp > M:
            break
print(cnt)