"""
hashmap 기본
"""
import sys

input = sys.stdin.readline
d = dict()
for _ in range(int(input())):
    a, *b = input().split()
    if a == 'add':
        d[b[0]] = b[1]
    elif a == 'remove':
        d.pop(b[0])
    else:
        print(d[b[0]] if b[0] in d else 'None')