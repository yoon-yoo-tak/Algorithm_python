"""
18436 수열과 쿼리 37
1 : A[i] = x
2 : 짝수의 갯수
3 : 홀수의 갯수
홀수 or 짝수 둘중 하나의 갯수만 저장해 놓고,
나머지는 r - l + 1 - (짝수 or 홀수) 의 갯수이다.
"""
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = ls[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

def sub_odd(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sub_odd(node * 2, start, mid, left, right) + sub_odd(node * 2 + 1, mid + 1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    mid = (start + end) // 2
    if start != end:
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


n = int(input())
ls = [i % 2 for i in list(map(int, input().split()))]
tree = [0] * 3000000
init(1, 0, n - 1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        # 홀에서 짝으로 바뀐다 > 해당 구간 -1
        # 짝에서 홀로 바뀐다 > 해당 구간  + 1
        if ls[b] and not c % 2:
            ls[b] = c % 2
            update(1, 0, n - 1, b, -1)
        elif not ls[b] and c % 2:
            ls[b] = c % 2
            update(1, 0, n - 1, b, 1)
    elif a == 2:
        print(c - b + 1 - sub_odd(1, 0, n - 1, b - 1, c - 1))
    elif a == 3:
        print(sub_odd(1, 0, n - 1, b - 1, c - 1))