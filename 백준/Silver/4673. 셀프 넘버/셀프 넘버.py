def d(n):
    val = n
    while n:
        val += n % 10
        n //= 10
    return val


nums = [True for _ in range(10036)]

for i in range(1, 10001):
    nums[d(i)] = False

for i in range(1, 10001):
    if nums[i]:
        print(i)
