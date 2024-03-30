# 문자열의 [::-1]를 이용하여 정답을 구한다.
def rev(num):
    return int(str(num)[::-1])


X, Y = map(int, input().split())

print(rev(rev(X) + rev(Y)))