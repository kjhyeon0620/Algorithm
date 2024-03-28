# bottom-up 방식으로 해결한다.

n = int(input())

arr = [0, 1] + [-1] * (n-1)

for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])