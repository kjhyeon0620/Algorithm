import sys


sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            if rank[rootA] == rank[rootB]:
                rank[rootA] += 1


n, m, = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(parent, rank, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("yes")
        else:
            print("no")
