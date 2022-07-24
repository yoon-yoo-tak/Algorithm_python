"""
1991 트리 순회

"""
import sys
from collections import deque
input = sys.stdin.readline

def pre_order(x):  # 전위 순회
    if x == -1:
        return
    print(chr(x + 65), end='')
    pre_order(child[x][0])
    pre_order(child[x][1])

def in_order(x):  # 중위 순회
    if x == -1:
        return
    in_order(child[x][0])
    print(chr(x + 65), end='')
    in_order(child[x][1])

def post_order(x):  # 후위 순회
    if x == -1:
        return
    post_order(child[x][0])
    post_order(child[x][1])
    print(chr(x + 65), end='')


n = int(input())
child = [[-1, -1] for _ in range(n)]

for _ in range(n):
    x, l, r = input().split()
    if l != '.':
        child[ord(x) - ord('A')][0] = ord(l) - ord('A')
    if r != '.':
        child[ord(x) - ord('A')][1] = ord(r) - ord('A')

pre_order(0)
print()
in_order(0)
print()
post_order(0)