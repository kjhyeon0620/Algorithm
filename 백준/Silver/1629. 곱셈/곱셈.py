# (A * B) % C = (A % C * B % C) % C

def solution(num1, num2):   # num1 ** num2 % C
    if num2 == 1:
        return num1 % C
    elif num2 % 2 == 0:
        return solution(num1, num2 // 2) ** 2
    else:
        return solution(num1, num2 // 2) ** 2 * num1 % C


A, B, C = map(int, input().split())
print(solution(A, B) % C)
