"""
2268 수들의 합 7
"""
import sys
input = sys.stdin.readline


def sub_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sub_sum(node * 2, start, mid, left, right) + sub_sum(node * 2 + 1, mid + 1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    mid = (start + end) // 2
    if start != end:
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


n, m = map(int, input().split())
ls = [0] * n
tree = [0] * 3000000
for _ in range(m):
    a, b, c = map(int, input().split())
    if a:
        b -= 1
        diff = c - ls[b]
        ls[b] = c
        update(1, 0, n - 1, b, diff)
    else:
        if b > c:
            b, c = c, b
        print(sub_sum(1, 0, n - 1, b - 1, c - 1))
