"""
16975 수열과 쿼리 21
레이지 세그
"""
import sys
input = sys.stdin.readline


def init(node, start ,end):
    if start == end:
        tree[node] = ls[start]
        return
    mid = (start + end ) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update(node, start, end, left, right, val):
    propagation(node, start, end)

    if right < start or left > end:
        return
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * val

        if start != end:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, val)
    update(node * 2 + 1, mid + 1, end, left, right, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def sub_sum(node, start, end, left, right):
    propagation(node, start, end)
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sub_sum(node * 2, start, mid, left, right) + sub_sum(node * 2 + 1, mid + 1, end, left, right)


def propagation(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0


n = int(input())
ls = list(map(int, input().split()))
tree = [0] * 3000000
lazy= [0] * 3000000
init(1, 0, n - 1)
m = int(input())
for _ in range(m):
    a, *b = map(int, input().split())
    if a == 1:
        update(1, 0, n - 1, b[0] - 1, b[1] - 1, b[2])
    elif a == 2:
        print(sub_sum(1, 0, n - 1, b[0] - 1, b[0] - 1))
