"""
2386 도비의 영어 공부

"""

import sys

input = sys.stdin.readline

while True:
    a, *b = input().split()
    if a == '#' and len(b) == 0:
        break
    count = 0
    for i in b:
        count += i.lower().count(a)
    print(a, count)
