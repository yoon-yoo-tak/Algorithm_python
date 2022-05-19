"""
4406 모음이 보이지 않는 사람
"""
for tt in range(1, int(input()) + 1):
    ans = ''.join([i for i in list(input()) if i not in ['a', 'e', 'i', 'o', 'u']])
    print(f'#{tt} {ans}')
