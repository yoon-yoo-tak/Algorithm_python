"""
4378 트ㅏㅊ;
"""

import sys

input = sys.stdin.readline
qwerty= ['1','2','3','4','5','6','7','8','9','0','-','=','Q','W','E','R','T','Y','U','I','O','P','[',']','\\',
         'A','S','D','F','G','H','J','K','L',';','\'','Z','X','C','V','B','N','M',',','.','/']

s = input().strip()
ans = ''
for i in s:
    if i in qwerty:
       ans += qwerty[qwerty.index(i) - 1]
    else:
        ans += ' '
print(ans)
