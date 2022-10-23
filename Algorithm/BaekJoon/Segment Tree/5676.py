"""
5676 음주 코딩
"""
import sys
input = sys.stdin.readline

def change(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

def init(node, start, end):
    if start == end:
        tree[node] = ls[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end)
    return tree[node]


def sub_mult(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sub_mult(n * 2, start, mid, left, right) * sub_mult(node * 2 + 1, mid + 1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = diff
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, index, diff)
    update(node * 2 + 1, mid + 1, end, index, diff)
    tree[node] = tree[node * 2] * tree[node * 2 + 1]


while True:
    try:
        n, k = map(int, input().split())
        ls = [change(i) for i in list(map(int, input().split()))]
        tree = [0] * 300000
        ans = ''
        init(1, 0, n - 1)
        for _ in range(k):
            a, b, c = input().split()
            b, c = int(b), int(c)
            if a == 'C':
                b -= 1
                c = change(c)
                ls[b] = c
                update(1, 0, n - 1, b, c)
            else:
                value = sub_mult(1, 0, n - 1, b - 1, c - 1)
                if value == 0:
                    ans += '0'
                elif value > 0:
                    ans += '+'
                else:
                    ans += '-'
        print(ans)
    except Exception:
        break
