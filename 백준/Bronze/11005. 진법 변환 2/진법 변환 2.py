# log를 활용해 B진법으로 변환했을 때의 자릿수를 구한다.
# 아스키코드를 통해 앞에서부터 하나씩 계산한다.


import math

N, B = map(int, input().split())
ans = ""

for i in range(int(math.log(N, B)), -1, -1):
    val = N // (B ** i)
    N -= val * (B ** i)
    if val > 9:
        ans += chr(val + 55)
    else:
        ans += str(val)

print(ans)