"""
2357 최솟값과 최댓값
"""
import sys
input = sys.stdin.readline

def init_max(node, start, end):
    if start == end:
        max_tree[node] = ls[start]
        return max_tree[node]
    mid = (start + end) // 2
    max_tree[node] = max(init_max(node * 2, start, mid), init_max(node * 2 + 1,mid + 1, end))
    return max_tree[node]

def init_min(node, start, end):
    if start == end:
        min_tree[node] = ls[start]
        return min_tree[node]
    mid = (start + end) // 2
    min_tree[node] = min(init_min(node * 2, start, mid), init_min(node * 2 + 1,mid + 1, end))
    return min_tree[node]

def sub_max(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    mid = (start + end) // 2
    return max(sub_max(node * 2, start, mid, left, right), sub_max(node * 2 + 1, mid + 1, end, left, right))
def sub_min(node, start, end, left, right):
    if left > end or right < start:
        return int(1e9) + 1
    if left <= start and end <= right:
        return min_tree[node]
    mid = (start + end) // 2
    return min(sub_min(node * 2, start, mid, left, right), sub_min(node * 2 + 1, mid + 1, end, left, right))

n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
max_tree = [0] * 3000000
min_tree = [0] * 3000000
init_max(1, 0, n - 1)
init_min(1, 0, n - 1)
for _ in range(m):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    print(sub_min(1, 0, n - 1, a, b), sub_max(1, 0, n - 1, a, b))
