"""
14428 수열과 쿼리 16
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

def init(node, start, end):
    if start == end:
        tree[node] = ls[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(node * 2, start, mid), init(node * 2 + 1, mid + 1, end))
    return tree[node]

def sub_min(node, start, end, left, right):
    mid = (start + end) // 2
    if left > end or right < start:
        return [INF, INF]
    if left <= start and end <= right:
        return tree[node]
    return min(sub_min(node * 2, start, mid, left, right), sub_min(node * 2 + 1, mid + 1, end, left, right))

def update(node, start, end, index, val):
    if index < start or index > end:
        return [INF, INF]
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


n = int(input())
a = list(map(int, input().split()))
m = int(input())
ls = []
for index, value in enumerate(a):
    ls.append([value, index + 1])

tree = [0] * 300000
init(1, 0, n - 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        ls[b - 1][0] = c
        update(1, 0, n - 1, b - 1, ls[b - 1])
    else:
        print(sub_min(1, 0, n - 1, b - 1, c - 1)[1])