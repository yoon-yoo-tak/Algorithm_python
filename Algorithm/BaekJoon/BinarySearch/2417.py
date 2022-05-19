"""
2417 정수 제곱근
"""

import sys
input = sys.stdin.readline
n = int(input())

def bisect(start, end, x):
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 < x:
            start = mid + 1
        else:
            end = mid - 1
    return start
print(bisect(0, n, n))