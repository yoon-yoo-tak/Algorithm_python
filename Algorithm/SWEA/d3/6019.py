"""
기차 사이의 파리
"""
for tt in range(1, int(input()) + 1):
    d, a, b, f = map(int, input().split())
    print(f'#{tt} {((d / (a + b))* f):.6f}')
