"""
10868 최솟값
"""
import sys
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = ls[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(node * 2, start, mid), init(node * 2 + 1, mid + 1, end))
    return tree[node]


def sub_min(node, start, end, left, right):
    if left > end or right < start:
        return 1000000001
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(sub_min(node * 2, start, mid, left, right), sub_min(node * 2 + 1, mid + 1, end, left, right))


n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
tree = [0] * 3000000

init(1, 0, n - 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(sub_min(1, 0, n - 1, a - 1, b - 1))
