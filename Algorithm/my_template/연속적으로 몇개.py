"""
배열안에서 이때까지 연속으로 몇개가 같은지
"""
import sys

input = sys.stdin.readline

ls = [3, 3, 2, 2, 2, 2, 1, 1, 3, 3, 3]
c = 1  # 이때까지 연속으로 몇개가 같은지?
lgst = 0
for i in range(1, len(ls)):
    if ls[i] == ls[i - 1]:
        c += 1
    else:
        c = 1
    lgst = max(lgst, c)
print(lgst)

