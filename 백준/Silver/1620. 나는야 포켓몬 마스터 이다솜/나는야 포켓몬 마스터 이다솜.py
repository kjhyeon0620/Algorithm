import sys


input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
names = dict()
nums = dict()
for i in range(1, N+1):
    pokemon = input().rstrip()
    names[i] = pokemon
    nums[pokemon] = i

for _ in range(M):
    inp = input().rstrip()
    if inp.isalpha():
        print(str(nums[inp]) + "\n")
    else:
        print(names[int(inp)] + "\n")
