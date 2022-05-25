"""
3376 파도반 수열
"""
for tt in range(1, int(input()) + 1):
    n = int(input())
    ls = [0] * 101
    ls[1] = 1
    ls[2] = 1
    ls[3] = 1
    for i in range(0, 98):
        ls[i + 3] = ls[i] + ls[i + 1]
    print(f'#{tt} {ls[n]}')