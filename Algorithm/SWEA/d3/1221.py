"""
1221 [S/W 문제해결 기본] 5일차 - GNS
"""
nums = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9
}

for tt in range(1, int(input()) + 1):
    a, b = input().split()
    b = int(b)
    ls = list(input().split())
    for i in range(len(ls)):
        ls[i] = [ls[i], nums[ls[i]]]
    ls = sorted(ls, key=lambda x: x[1])
    print(a)
    for i in ls:
        print(i[0], end=' ')
    print()



