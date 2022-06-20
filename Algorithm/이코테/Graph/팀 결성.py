"""
이코테 그래프 이론 연습문제 1 - 팀 결성
"""
import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for i in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union(a, b)
    elif oper == 1:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')