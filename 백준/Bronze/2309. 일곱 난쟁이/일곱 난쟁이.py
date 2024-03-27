# 먼저 9개의 합을 구한 후, 100을 뺀다.
# 9개의 숫자 중 2개의 숫자를 골라서 합이 위에서 뺀 숫자인 조합을 고른다.
# 위에서 나온 2개를 뺀 나머지 7개를 출력한다.

heights = [int(input()) for _ in range(9)]
heights.sort()
findSum = sum(heights) - 100
flag = False

for i in range(9):
    if flag:
        break
    for j in range(i+1, 9):
        if heights[i] + heights[j] == findSum:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(heights[k])
            flag = True
            break