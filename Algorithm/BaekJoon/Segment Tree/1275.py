import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = ls[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    mid = (start + end) // 2
    if start != end:
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)

def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)


n, q = map(int, input().split())
ls = list(map(int, input().split()))
tree = [0] * 3000000
init(1, 0, n - 1)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(query(1, 0, n - 1, x - 1, y - 1))
    a -= 1
    diff = b - ls[a]
    ls[a] = b
    update(1, 0, n - 1, a, diff)
