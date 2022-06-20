n=int(input())
ls=[list(map(int,input().split())) for _ in range(n)]
a=[int(1e10) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        dist=sorted([abs(ls[i][0]-ls[k][0])+abs(ls[j][1]-ls[k][1]) for k in range(n)])
        total=0
        for k in range(n):
            total+=dist[k]
            a[k+1] = min(a[k+1],total)
print(*a[1:])