# 달의 일수를 모두 더한 후 7로 나눈 나머지를 이용해 요일을 구한다.

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
sumOfDays = sum(months[:x]) + y
print(days[((sumOfDays % 7)-1)])