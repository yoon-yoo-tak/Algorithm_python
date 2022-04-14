t = int(input())
for i in range(1, t + 1):
    n = int(input())
    ls = sorted(map(int, input().split()))
    print(f'#{i}',end=' ')
    print(*ls)