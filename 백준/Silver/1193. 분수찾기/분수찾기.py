# 분자 : 1 1 2 3 2 1 1 2 3 4 5 4 3 2 1
# 분모 : 1 2 1 1 2 3 4 3 2 1 1 2 3 4 5
# 1 / 2,3 / 4,5,6 / 7,8,9,10/ 11,12,13,14,15
# 1   2     3         4        5
#           layer 짝수
# 분자 : (X - start) + 1
# 분모 : (end - X) + 1
# layer가 홀수면 반대로

X = int(input())
end = 0
layer = 1
while True:
    end += layer
    if end >= X:
        break
    layer += 1
start = end - layer + 1
if layer % 2 == 0:
    print(f'{X-start+1}/{end-X+1}')
else:
    print(f'{end-X+1}/{X-start+1}')



