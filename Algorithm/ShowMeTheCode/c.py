l = []

for i in range(8):
    n = int(input())
    l.append([n, i])


l.sort(key=lambda num: num[0])

max_sum = 0
idx = []

for i in range(3, 8):
    max_sum += l[i][0]
    idx.append(l[i][1])

idx.sort()
print(max_sum)

for i in range(5):
    print(idx[i]+1, end = ' ')