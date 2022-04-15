"""
12904 A와B
"""
import sys

input = sys.stdin.readline
s = list(input().strip())
t = list(input().strip())
flag = False

while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]
    if s == t:
        flag = True
        break
print(1 if flag else 0)