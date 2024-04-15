# 해당하는 주유소의 가격보다 낮은 가격의 주유소까지 기름을 넣고 이동한다.
# 마지막 도시까지 위를 반복한다.

import sys


input = sys.stdin.readline
N = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))
ans = lengths[0] * prices[0]    # 첫 주유소에서 반드시 다음 도시까지 충전해야함
minPrice = prices[0]

for i in range(1, N-1):
    minPrice = min(minPrice, prices[i])
    ans += minPrice * lengths[i]
    
print(ans)
