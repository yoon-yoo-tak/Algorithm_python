"""
14438 수열과 쿼리 17
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
        return int(1e9) + 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(sub_min(node * 2, start, mid, left, right), sub_min(node * 2 + 1, mid + 1, end, left, right))


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    mid = (start + end) // 2
    if start != end:
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


n = int(input())
ls = list(map(int, input().split()))
tree = [0] * 3000000
init(1, 0, n - 1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - ls[b]
        ls[b] = c
        update(1, 0, n - 1, b, diff)
    else:
        print(sub_min(1, 0, n - 1, b - 1, c - 1))
