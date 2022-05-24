"""
9280 다솔이의 월급 상자

"""
t = int(input())
for tt in range(1, t + 1):
    n = int(input())
    total = 0
    for _ in range(n):
        a, b = map(float, input().split())
        total += a * b
    print(f'#{tt} {total:.6f}')
