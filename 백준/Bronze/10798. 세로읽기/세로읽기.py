# 각 문자열의 길이를 리스트로 저장해둔 후 첫 번째 인덱스부터 하나씩 ans 변수에 문자를 더한다.

inputs = []
lengths = []
ans = ""

for i in range(5):
    inputs.append(input())
    lengths.append(len(inputs[i]))

for i in range(max(lengths)):
    for j in range(5):
        if i < lengths[j]:
            ans += inputs[j][i]

print(ans)