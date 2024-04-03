# 등급에 따른 과목평점을 dictionary에 저장한 후 계산한다.

scores = dict({"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
              "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0})
totalGrade = 0
ans = 0.0
for _ in range(20):
    title, grade, score = input().split()
    if score != "P":
        ans += scores[score] * float(grade)
        totalGrade += float(grade)

print(ans / totalGrade)
