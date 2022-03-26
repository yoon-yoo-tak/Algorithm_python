"""

5800 성적 통계

"""
import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, *a = map(int, input().split())
    print('Class {}'.format(i + 1))
    a.sort(reverse = True)
    max_gap = 0
    for i in range(len(a) - 1):
        g = a[i] - a[i + 1]
        max_gap = max(max_gap, g)
    print('Max {max}, Min {min}, Largest gap {gap}'.format(max=max(a), min=min(a), gap=max_gap))

