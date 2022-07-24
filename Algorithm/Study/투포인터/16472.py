"""
16472 고냥이
"""
import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()

cnt = [0] * 30
kind = 0

def add(x):
    global kind
    t = ord(x) - ord('a')
    cnt[t] += 1
    if cnt[t] == 1:
        kind += 1
def remove(x):
    global kind
    t = ord(x) - ord('a')
    cnt[t] -= 1
    if cnt[t] == 0:
        kind -= 1
l, ans = 0, 0
for i in range(len(s)):
    add(s[i])
    while kind > n:
        remove(s[l])
        l += 1
    ans = max(ans, i - l + 1)
print(ans)