"""
21756 지우개

"""

import sys

input = sys.stdin.readline
n = int(input())
ls = [x + 1 for x in range(n)]
while len(ls) > 1:
    idx = []
    for i in range(len(ls)):
        if i % 2 == 0:
            idx.append(i)
    idx.sort(reverse=True)
    for i in idx:
        ls.pop(i)
print(ls[0])
