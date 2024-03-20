# 숫자를 입력 받아 소수인지 확인하는 함수를 통해 소수라면 개수에 추가한다.
# 함수 -> 2부터 해당 숫자의 제곱근 이하의 숫자까지 해당 숫자의 약수가 없다면 소수이다.

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


N = int(input())
arr = map(int, input().split())
ans = 0

for el in arr:
    if isPrime(el):
        ans += 1
        
print(ans)