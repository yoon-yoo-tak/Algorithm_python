"""
13428 숫자 조작
"""
t = int(input())
for tt in range(1, t + 1):
    s = list(input())
    max_val = int(''.join(s))
    min_val = int(''.join(s))
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            s[i], s[j] = s[j], s[i]
            num = ''.join(s)
            if len(str(int(num))) == len(s):
                max_val = max(max_val, int(num))
                min_val = min(min_val, int(num))
            s[i], s[j] = s[j], s[i]
    print(f'#{tt} {min_val} {max_val}')

