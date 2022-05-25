"""
3975 승률 비교하기
"""
res = ['']
for tt in range(1, int(input()) + 1):
    a, b, c, d = map(int, input().split())
    if a / b == c / d:
        res.append('DRAW')
    elif a / b < c / d:
        res.append('BOB')
    else:
        res.append('ALICE')

for i in range(1, len(res)):
    print(f'#{i} {res[i]}')
