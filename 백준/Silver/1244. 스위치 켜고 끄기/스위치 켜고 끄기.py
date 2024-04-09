# 주어진 조건에 따라 스위치를 켜고 끈다.

def switch(lst, idx):
    if lst[idx] == 1:
        lst[idx] = 0
    else:
        lst[idx] = 1


S = int(input())
board = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    gen, num = map(int, input().split())

    if gen == 1: # 남학생
        tmp = num-1
        while tmp < S:
            switch(board, tmp)
            tmp += num
    else:
        switch(board, num-1)
        for i in range(1, S//2+1):
            if 0 > num-1-i or S <= num-1+i:
                break
            if board[num-1-i] != board[num-1+i]:
                break
            switch(board, num-1+i)
            switch(board, num-1-i)

for i in range(S):
    if i % 20 == 19:
        print(board[i])
    else:
        print(board[i], end=" ")