def findDivisor(num):
    cnt = 0
    arr = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt += 1
            arr.append(i)
    for i in range(cnt, 0, -1):
        arr.append(num // arr[i])
    return arr


while True:
    inp = int(input())

    if inp == -1:
        break
    divisors = findDivisor(inp)
    sumOfDivisor = sum(divisors)
    if sumOfDivisor == inp:
        print(str(inp) + " = ", end="")
        length = len(divisors)
        for i in range(length):
            if i == length-1:
                print(divisors[i])
            else:
                print(str(divisors[i]) + " + ", end = "")
    else:
        print(str(inp) + " is NOT perfect.")
