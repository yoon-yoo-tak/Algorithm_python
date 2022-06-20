n, m = map(int, input().split())

selected = [0] * m
def rec(x):
    if x == m:
        print(*selected)
        return
    else:
        start = 1 if x == 0 else selected[x - 1]
        for i in range(start, n + 1):
            selected[x] = i
            rec(x + 1)
            selected[x] = 0
rec(0)