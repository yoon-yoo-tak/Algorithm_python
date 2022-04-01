"""
1342 행운의 문자열

"""

import sys

input = sys.stdin.readline

s = input().strip()
s = list(s)
su = len(s)
count = 0
alphabet = [0,0,0,0,0,
            0,0,0,0,0,
            0,0,0,0,0,
            0,0,0,0,0,
            0,0,0,0,0,
            0]

for i in range(len(s)):
    alphabet[ord(str(s[i])) - 97] += 1

def backtracking(l, p):
    global count
    if l == 0:
        count += 1
    for i in range(26):
        if alphabet[i] > 0 and i != p:
            alphabet[i] -= 1
            backtracking(l-1, i)
            alphabet[i] += 1
        else:
            pass

backtracking(su, -1)
print(count)