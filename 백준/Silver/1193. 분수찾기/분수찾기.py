# 분자 : 1 1 2 3 2 1 1 2 3 4 5 4 3 2 1
# 분모 : 1 2 1 1 2 3 4 3 2 1 1 2 3 4 5
# 1 / 2,3 / 4,5,6 / 7,8,9,10/ 11,12,13,14,15
# 1   2     3         4        5 -> layer
#           layer 짝수
# 분자 : (X - start) + 1
# 분모 : (end - X) + 1
# layer가 홀수면 반대로

X = int(input())
end = 0 # end -> 해당 layer에서 가장 큰 값
layer = 1
while True: # X가 해당하는 layer를 찾는다.
    end += layer
    if end >= X:
        break
    layer += 1
start = end - layer + 1 # start -> 해당 layer에서 가장 작은 값
if layer % 2 == 0:
    print(X - start + 1, end="")
    print("/", end="")
    print(end - X + 1)
else:
    print(end - X + 1, end="")
    print("/", end="")
    print(X - start + 1)


