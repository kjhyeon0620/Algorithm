# 1. 숫자를 10번 입력받고, 각각 42로 나눈 나머지를 set에 저장한다.
# 2. set의 크기를 출력한다.

ans = set()

for i in range(10):
    inp = int(input())
    ans.add(inp % 42)

print(len(ans))
