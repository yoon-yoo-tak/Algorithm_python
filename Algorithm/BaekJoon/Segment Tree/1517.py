"""
1517 버블 소트
inversion count
"""
import sys
from collections import defaultdict
input = sys.stdin.readline


def sub_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sub_sum(node * 2, start, mid, left, right) + sub_sum(node * 2 + 1, mid + 1, end, left, right)


def update(node, start, end, idx, diff):
    if start == end:
        tree[node] = diff
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(node * 2, start, mid, idx, diff)
    else:
        update(node * 2 + 1, mid + 1, end, idx, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


n = int(input())
ls = list(map(int, input().split()))
tree = [0] * 3000000
pos = defaultdict(int)
index = sorted(ls)
for i in range(n):
    pos[ls[i]] = i
ans = 0

for i in range(n):
    idx = pos[index[i]]
    ans += sub_sum(1, 0, n - 1, idx + 1, n - 1)
    update(1, 0, n - 1, idx, 1)
print(ans)