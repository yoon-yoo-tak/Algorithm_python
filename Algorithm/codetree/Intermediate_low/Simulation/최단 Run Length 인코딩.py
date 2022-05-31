"""
최단 Run Length 인코딩
"""
import sys

input = sys.stdin.readline

s = list(input().strip())

def shift():
    global ans
    temp = s[-1]
    for i in range(len(s) - 1, 0, -1):
        s[i] = s[i - 1]
    s[0] = temp
    ans = min(ans, len(encoding()))

def encoding():
    temp = ''
    seq = 1
    temp_char = s[0]
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            seq += 1
        else:
            temp += temp_char + str(seq)
            seq = 1
            temp_char = s[i + 1]
    temp += temp_char + str(seq)
    return temp
ans = int(1e9)
for _ in range(len(s)):
    shift()

print(ans)