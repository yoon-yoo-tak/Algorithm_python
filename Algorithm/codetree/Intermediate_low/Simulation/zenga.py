"""
1차원 젠가
"""
import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
total_block_cnt = n

def cut_array(s, e):
    global total_block_cnt
    temp = []
    for i in range(total_block_cnt):
        if not (s <= i <= e):
            temp.append(a[i])
    total_block_cnt = len(temp)
    for i in range(total_block_cnt):
        a[i] = temp[i]

def simulate():
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    cut_array(start, end)
simulate()
simulate()
print(total_block_cnt)
for i in range(total_block_cnt):
    print(a[i])




