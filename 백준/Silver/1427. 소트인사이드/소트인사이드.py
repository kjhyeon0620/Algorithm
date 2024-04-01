# 문자열로 입력받은 후 숫자를 하나씩 분리하여 리스트로 저장한다.
# sort를 이용하여 정렬한다.

N = input()
N = list(map(int, N))
N.sort(reverse=True)

for el in N:
    print(el, end="")
