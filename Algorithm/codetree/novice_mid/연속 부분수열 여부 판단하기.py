"""


"""

import sys

input = sys.stdin.readline

a, b = map(int, input().split())
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))

for i in range(a - b):
    if ls1[i:i + b] == ls2:
        print('Yes')
        sys.exit()
print('No')