"""
바구니 안의 사탕 2
"""
import sys

input = sys.stdin.readline

MAX_NUM = 100


n, k = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    a, x = tuple(map(int, input().split()))
    arr[x] = a


max_sum = 0
for i in range(MAX_NUM):

    sum_all = 0
    for j in range(i - k, i + k + 1):
        if j >= 0 and j <= MAX_NUM:
            sum_all += arr[j]


    max_sum = max(max_sum, sum_all)

print(max_sum)