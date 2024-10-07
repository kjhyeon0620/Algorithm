N = int(input())

idx = dict()
books = []
cnt = 0

for _ in range(N):
    b = input()
    if idx.get(b) is None:
        books.append([1, b])
        idx[b] = cnt
        cnt += 1
    else:
        books[idx[b]][0] += 1
        
books.sort(key=lambda x: (-x[0], x[1]))
print(books[0][1])
