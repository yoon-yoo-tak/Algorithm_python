"""
3408 세가지 합 구하기
"""
for tt in range(1, int(input()) + 1):
    n = int(input())
    s1 = (n *(n + 1)) // 2
    s2 = n ** 2
    s3 = n ** 2 + n
    print(f'#{tt} {s1} {s2} {s3}')
