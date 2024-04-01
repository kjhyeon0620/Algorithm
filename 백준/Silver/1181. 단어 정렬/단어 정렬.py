# 데이터를 set에 저장하여 중복을 제거한다.
# sort와 lambda를 활용하여 조건에 맞게 정렬한 후 출력한다.

import sys


input = sys.stdin.readline
N = int(input())
words = list(set(input().strip() for _ in range(N)))
words.sort(key=lambda x: (len(x), x))
print("\n".join(words))