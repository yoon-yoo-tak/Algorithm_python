"""
10059 유효기간
"""
t = int(input())
for tt in range(1, t + 1):
    s = input()
    front = int(s[:2])
    back = int(s[2:])
    res = ''
    if front > 12 and back <= 12:
        res = 'YYMM'
    elif back > 12 and front <= 12:
        res = 'MMYY'
    elif front <= 12 and back <= 12:
        res = 'AMBIGUOUS'
    elif front > 12 and back > 12:
        res = 'NA'
    print(f'#{tt} {res}')