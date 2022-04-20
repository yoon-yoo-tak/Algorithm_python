"""
12871 무한 문자열
"""

import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
for i in range(len(s1) * len(s2)):
    if s1[i % len(s1)] != s2[i % len(s2)]:
        print(0)
        break
else:
    print(1)