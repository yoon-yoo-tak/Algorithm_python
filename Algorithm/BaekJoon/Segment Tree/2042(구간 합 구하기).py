"""
2042 구간 합 구하기
"""
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = ls[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

def sub_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return sub_sum(node * 2, start, (start + end) // 2, left, right) + sub_sum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:  # 범위에 포함 안되면 업데이트 안함.
        return
    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

n, m, k = map(int, input().split())
ls = [int(input()) for _ in range(n)]
tree = [0] * int(3e6)
init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1  # 인덱스
        diff = c - ls[b]  # 차이만큼 더해준다.
        ls[b] = c  # 원래 배열 바꿔주고
        update(1, 0, n - 1, b, diff) # 1번 노드부터 시작해서
    else:
        print(sub_sum(1, 0, n - 1, b - 1, c - 1))