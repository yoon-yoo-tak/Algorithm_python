"""
16171 나는 친구가 적다(small)
"""

import sys

input = sys.stdin.readline
s = input().strip()
k = input().strip()
s = ''.join([i for i in s if i.isalpha()])
print(1 if k in s else 0)