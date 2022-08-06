"""
2243 사탕 상자
"""
import sys

input = sys.stdin.readline

def update(node, start, end, target, value):
    if target < start or target > end:
        return tree[node]
    if start == end == target:
        tree[node] += value
        ls[node] = target
        return tree[node]
    mid = (start + end) // 2
    tree[node] = update(node * 2, start, mid, target , value) + update(node * 2 + 1, mid + 1, end, target, value)
    return tree[node]

def kth(node, start, end, value):
    if start == end:
        tree[node] -= 1
        print(ls[node])
        return tree[node]
    l = tree[node * 2]
    mid = (start + end) // 2
    if l >= value:
        kth(node * 2, start, mid, value)
    else:
        kth(node * 2 + 1, mid + 1, end, value - tree[node * 2])
    tree[node] = tree[node * 2] +  tree[node * 2 + 1]
    return tree[node]


n = int(input())
tree = [0] * 3000003
ls = [0] * 3000003
for _ in range(n):
    a, *b = map(int, input().split())
    if a == 1:
        kth(1, 1, 1000000, b[0])
    else:
        update(1, 1, 1000000, b[0], b[1])