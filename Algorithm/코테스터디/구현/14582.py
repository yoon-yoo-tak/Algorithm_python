"""
14582 오늘도 졌다
"""
import sys

input = sys.stdin.readline

woolim = list(map(int, input().split())) + [0]
start_link = [0] + list(map(int, input().split()))
ans = 'No'
total_w, total_s = 0, 0
for i in range(10):
    total_w += woolim[i]
    total_s += start_link[i]
    if total_w > total_s:
        ans = 'Yes'
        break
print(ans)
