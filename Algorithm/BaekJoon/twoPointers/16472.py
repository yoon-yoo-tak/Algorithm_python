"""

16472 고냥이

"""
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

cnt = [0] * 30
k = 0

def add(x):
    global k
    t = ord(x) - ord('a')
    cnt[t] += 1
    if cnt[t] == 1:
        k += 1

def remove(x):
    global k
    t = ord(x) - ord('a')
    cnt[t] -= 1
    if cnt[t] == 0:
        k -=1

l = 0
ans = 0
for i in range(len(s)):
    add(s[i])
    while k > n:
        remove(s[l])
        l += 1
    ans = max(ans, i - l + 1)

print(ans)