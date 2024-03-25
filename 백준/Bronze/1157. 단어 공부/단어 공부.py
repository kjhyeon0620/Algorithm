# 각 원소가 0인 26 크기의 list 를 만든다.
# 입력 문자를 모두 대문자로 변환한다.
# 각 문자의 (아스키코드 - 65)의 index에 해당하는 값을 증가시킨다.
# 최댓값의 index를 구하여 가장 많이 사용된 알파벳을 구한다.
# 최댓값의 개수를 구하여 2 이상인 경우 ? 를 출력한다.

alphabets = [0] * 26
word = input().upper()

for ch in word:
    alphabets[ord(ch) - 65] += 1
    
maxValue = max(alphabets)

if alphabets.count(maxValue) > 1:
    print("?")
else:
    print(chr(alphabets.index(maxValue) + 65))