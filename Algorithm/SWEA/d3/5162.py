"""
5162 두가지 빵의 딜레마
"""
for tt in range(int(input())):
    a, b, c = map(int, input().split())
    if a >= b:
        ans = c // b
        print(f'#{tt + 1} {ans}')
    else:
        ans = c // a
        print(f'#{tt + 1} {ans}')