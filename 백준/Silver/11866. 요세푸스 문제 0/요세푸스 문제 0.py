# list 의 remove를 통해 해당하는 원소를 삭제한다.
# % 를 이용해 양 끝을 연결한다.

N, K = map(int, input().split())
ans = []
arr = list(range(1, N+1))
length = N
tmp = 0
for i in range(N):
    tmp = (tmp+K-1) % length
    ans.append(arr[tmp])
    arr.remove(arr[tmp])
    length -= 1

print("<" + ", ".join(map(str, ans)) + ">")
