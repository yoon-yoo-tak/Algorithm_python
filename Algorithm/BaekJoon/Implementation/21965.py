"""

21965

"""
import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
a = 1
for i in range(len(ls)):
    if i > 0:
        if ls[i] > ls[i - 1]:
            a = ls[i]
        if i == n - 1:
            print('YES')
            break

        if a > ls[i]:
            if ls[i] <= ls[i + 1]:
                print('NO')
                break
            if i == n - 1:
                print('YES')
        if ls[i] == ls[i - 1]:
            print('NO')
            break