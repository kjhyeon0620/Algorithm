import sys
import bisect


def binary_search(ordered_list, func_target):
    index = bisect.bisect_left(ordered_list, func_target)

    if index < len(ordered_list) and ordered_list[index] == func_target:
        return index
    else:
        return None


# sys.stdin = open('bj1920_in.txt', 'r')
N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
target = list(map(int, input().split()))
for j in target:
    search_value = binary_search(card, j)
    if search_value is None:
        print(0)
    else:
        print(1)
