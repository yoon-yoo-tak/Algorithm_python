"""
21966 (중략)
"""

import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()

if n <= 25:
    print(s)
else:
    tmp = s[11:-11]
    if '.' in tmp:  # . 3개
        if tmp[-1] == '.' and tmp.count('.') == 1:
            front = s[:11]
            back = s[-11:]
            print(front + '...' + back)
        else:  # . 6개
            front = s[:9]
            back = s[-10:]
            print(front + '......'+back)
    else:  # . 3개
        front = s[:11]
        back = s[-11:]
        print(front + '...' + back)