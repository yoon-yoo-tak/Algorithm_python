"""
10200 구독자전쟁
"""
t = int(input())

for num in range(t):
    n,a,b = map(int,input().split())

    if a+b <= n:
        max_n = min(a,b)
        min_n = 0
    elif a+b > n:
        max_n = min(a, b)
        min_n = a+b-n
    if a==b and b==n:
        max_n = n
        min_n = n
    print('#{} {} {}'.format(num+1,max_n,min_n))