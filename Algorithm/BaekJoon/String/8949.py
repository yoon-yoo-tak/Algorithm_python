"""
8949 대충 더해

"""

import sys

input = sys.stdin.readline


a, b = input().split()
a = a[::-1]
b = b[::-1]
result = []
if len(a) >= len(b):
    for i in range(len(b)):
        result.append(str(int(a[i]) + int(b[i])))
    result += a[len(b):]
else:
    for i in range(len(a)):
        result.append(str(int(a[i]) + int(b[i])))
    result += b[len(a):]
result.reverse()
print(''.join(result))