"""
11652 카드

N개중 가장 많이 등장한 숫자 출력

"""
import sys
input = sys.stdin.readline

ls = []
for i in range(int(input())):
    ls.append(int(input()))
ls.sort()

mode = ls[0]
modeCnt = 1
curCnt = 1

for i in range(1, len(ls)):
    if ls[i] == ls[i - 1]:
        curCnt += 1
    else:
        curCnt = 1
    if modeCnt < curCnt:
        modeCnt = curCnt
        mode = ls[i]
print(mode)
