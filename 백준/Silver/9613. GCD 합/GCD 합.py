# 최대공약수를 구하는 함수를 만든다
# 모든 쌍에 대하여 위 함수를 실행시키고 합을 구한다

def findGcd(num1, num2):
    while num2 > 0:
        if num1 < num2:
            num1, num2 = num2, num1
        num1, num2 = num2, num1 % num2

    return num1


t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    total = 0
    for i in range(1, nums[0]):
        for j in range(i+1, nums[0]+1):
            total += findGcd(nums[i], nums[j])
    print(total)
