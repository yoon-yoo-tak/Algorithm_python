"""
13736 사탕 분배
"""

for t in range(1,int(input())+1):
    a,b,k = map(int,input().split())
    c = a+b
    n = 1
    for i in range(31,-1,-1):
        n *= n
        if k & (1<<i):
            n<<=1
        n %= c
    a = (a*n)%c
    b = c-a
    print("#%d"%t, min(a,b))