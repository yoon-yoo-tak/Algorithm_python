
n, k = map(int, input().split())
ls =[[] for _ in range(n)]
for i in range(n):
    a, b, c = map(int, input().split())
    ls[i].append((a, 0))
    ls[i].append((b, 0))
    ls[i].append((c, 0))

ls[1][0][0] = ls[0][0][0] + 1
print(ls)

