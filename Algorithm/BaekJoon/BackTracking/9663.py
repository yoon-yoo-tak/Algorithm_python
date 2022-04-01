"""
9663 N-Queen

"""

import sys

input = sys.stdin.readline

def nQueen(depth):
    global count
    if depth == n:
        count += 1
        return
    for i in range(n):
        arr[depth] = i
        if possible(depth):
            nQueen(depth + 1)

def possible(col):
    for i in range(col):
        if arr[col] == arr[i]:
            return False
        elif abs(col - i) == abs(arr[col] - arr[i]):
            return False
    return True

n = int(input())
arr = [0] * n
count = 0
nQueen(0)
print(count)
