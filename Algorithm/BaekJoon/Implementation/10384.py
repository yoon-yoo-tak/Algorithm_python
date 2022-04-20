"""
10384 팬그램
"""

import sys, re

input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    ls = [0] * 26
    s = input().split()
    s = ''.join(s).upper()
    for ss in s:
        if ss.isalpha():
            ls[ord(ss) - 65] += 1
    if min(ls) == 0:
        print(f'Case {i}: Not a pangram')
    elif min(ls) == 1:
        print(f'Case {i}: Pangram!')
    elif min(ls) == 2:
        print(f'Case {i}: Double pangram!!')
    elif min(ls) == 3:
        print(f'Case {i}: Triple pangram!!!')

