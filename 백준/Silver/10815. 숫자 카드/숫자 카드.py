N = int(input())
hasCards = set(list(map(int, input().split())))
M = int(input())
findCards = list(map(int, input().split()))

for fc in findCards:
    if fc in hasCards:
        print("1", end=" ")
    else:
        print("0", end=" ")
