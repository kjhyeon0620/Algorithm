# 30의 배수의 조건 :
# 일의 자리가 0
# 일의 자리를 뺀 나머지 수가 3의 배수 -> 각 자릿수를 더했을 때 3의 배수

N = list(map(int, input()))
N.sort(reverse=True)
if N[-1] != 0:
    print(-1)
elif sum(N) % 3 != 0:
    print(-1)
else:
    print("".join(map(str, N)))
