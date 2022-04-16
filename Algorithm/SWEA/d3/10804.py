"""
10804 거울상
"""
t = int(input())
for tt in range(1, t + 1):
    s = list(input())[::-1]
    for i in range(len(s)):
        if s[i] == 'b':
            s[i] = 'd'
        elif s[i] == 'd':
            s[i] = 'b'
        elif s[i] == 'p':
            s[i] = 'q'
        else:
            s[i] = 'p'
    print(f'#{tt} {"".join(s)}')

