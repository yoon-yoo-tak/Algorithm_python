from collections import deque

a = dict()
for _ in range(3):
    c, d = input().split()
    a[c] = d
ls = 0
for i in a.keys():
    ls = i
print(type(ls))