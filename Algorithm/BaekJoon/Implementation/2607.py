"""
2607 비슷한 단어
"""

import sys

input = sys.stdin.readline

n = int(input())
words = [[0 for _ in range(26)] for _ in range(n)]
for i in range(n):
    s = input().strip()
    for ss in s:
        words[i][ord(ss) - ord('A')] += 1

ans = 0

for word in words[1:]:
    a, b = 0, 0
    for i in range(26):
        if word[i] > words[0][i]:
            a += (word[i] - words[0][i])
        else:
            b += (words[0][i] - word[i])
    if a < 2 and b < 2:
        ans += 1
print(ans)