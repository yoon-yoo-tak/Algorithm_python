"""
5766 할아버지는 유명해!
"""

import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ls = []
    for i in range(n):
        temp = list(map(int, input().split()))
        for num in temp:
            ls.append(num)
    record = set()
    for i in ls:
        record.add((i, ls.count(i)))
    record = sorted(record, key=lambda x: (-x[1], x[0]))
    max_record = record[0][1]
    for x, y in record:
        if y != max_record:
            sec = y
            break
    for x, y in record:
        if y == sec:
            print(x, end=' ')
