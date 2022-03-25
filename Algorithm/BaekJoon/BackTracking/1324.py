"""
1324 행운의 문자열

각 문자에 대해 인접한 문자가 다르다면 행운의 문자열
"""
from itertools import permutations

ls = [i for i in input()]
perm = permutations(ls, len(ls))
lucky_str = []
def isLucky(s):
    bol = False
    for i in range(len(s)):
        if i == 0:
            if s[i] != s[i+1]:
                bol = True
            else:
                bol = False
                break
        elif i == len(s)-1:
            if s[i] != s[i-1]:
                bol = True
            else:
                bol = False
                break
        else:
            if s[i] != s[i+1] and s[i] != s[i-1]:
                bol = True
            else:
                bol = False
                break
    return bol

for p in perm:
    new_str = "".join(p)
    if isLucky(new_str):
        lucky_str.append(new_str)
print(len(lucky_str))