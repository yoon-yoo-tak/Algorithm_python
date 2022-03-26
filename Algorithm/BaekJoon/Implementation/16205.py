"""

16205 변수명

"""
import sys
input = sys.stdin.readline

a, b = input().split()

if a == '1':
    for i in b:
        if 65 <= ord(i) <= 90:
            c = i.lower
            d = '_'
            d += c
            b = b.replace(i, d)
        