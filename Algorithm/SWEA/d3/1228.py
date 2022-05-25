"""
1228 [S/W 문제해결 기본] 8일차 - 암호문1
"""
for tt in range(1, 11):
    n = int(input())
    ls = list(map(int, input().split()))
    order = int(input())
    data = list(input().split('I'))
    data = data[1:]
    for i in range(len(data)):
        data[i] = data[i].split()
    for i in data:
        x, y, s = int(i[0]), int(i[1]), [int(num) for num in i[2:]]
        ls = ls[:x] + s + ls[x:]


    print(f'#{tt}', end=' ')
    print(*ls[:10])

